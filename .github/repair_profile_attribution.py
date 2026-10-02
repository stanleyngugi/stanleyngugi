"""Prepare a history-preserving profile authorship correction in a local clone.

Only Codex author/committer identities are changed. Trees, messages, dates and
Stanley's existing identities are retained. Nothing is pushed by this script.
"""
import os
import pathlib
import re
import subprocess
import sys

repo = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
def git(*args, input=None, env=None):
    return subprocess.check_output(['git', '-C', str(repo), *args], input=input, env=env)

expected = '039f40214eb65de14a431e4dd839075c91212a55'
head = git('rev-parse', 'main').decode().strip()
if head != expected:
    raise SystemExit('The profile branch moved; fetch and review it before rewriting.')
owner_name = git('show', '-s', '--format=%an', head).decode().strip()
owner_email = git('show', '-s', '--format=%ae', head).decode().strip()
if owner_name != 'Stanley Ngugi':
    raise SystemExit('Unexpected owner identity; stop for review.')
replacements = {}
changed = 0
for sha in git('rev-list', '--reverse', 'main').decode().split():
    raw = git('cat-file', '-p', sha)
    headers, message = raw.split(b'\n\n', 1)
    lines = headers.decode().splitlines()
    tree = next(x[5:] for x in lines if x.startswith('tree '))
    parents = [x[7:] for x in lines if x.startswith('parent ')]
    env = os.environ.copy()
    for kind in ('author', 'committer'):
        line = next(x[len(kind)+1:] for x in lines if x.startswith(kind+' '))
        name, email, stamp, zone = re.fullmatch(r'(.*) <([^>]+)> (\d+) ([+-]\d{4})', line).groups()
        if name == 'Codex':
            name, email = owner_name, owner_email
            changed += 1
        prefix = 'GIT_'+kind.upper()+'_'
        env[prefix+'NAME'] = name
        env[prefix+'EMAIL'] = email
        env[prefix+'DATE'] = '@'+stamp+' '+zone
    args = ['commit-tree', tree]
    for parent in parents:
        args += ['-p', replacements.get(parent, parent)]
    replacements[sha] = git(*args, input=message, env=env).decode().strip()
new_head = replacements[head]
if git('rev-parse', head+'^{tree}') != git('rev-parse', new_head+'^{tree}'):
    raise SystemExit('Tree changed unexpectedly; stop.')
git('update-ref', 'refs/heads/attribution-repair', new_head)
if b'Codex' in git('log', '--format=%an %cn', 'attribution-repair'):
    raise SystemExit('Codex identity remains; stop.')
print('Prepared', len(replacements), 'commits; corrected', changed//2, 'Codex-authored commits.')
print('README/tree unchanged. New branch: attribution-repair.')
print('To publish after reviewing the history:')
print('git push --force-with-lease=refs/heads/main:'+expected+' origin attribution-repair:main')

