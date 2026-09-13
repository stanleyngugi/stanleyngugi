# Stanley Ngugi

Independent AI researcher working on post-training with reinforcement learning, RL environments, and formal verification.

## Current work

### [MathCheck RL](https://github.com/stanleyngugi/mathcheck-rl)

An answer-key-free RL environment for bounded mathematical tasks. Models submit an answer or complete finite certificate; a frozen specification and Lean-backed checker determine the reward. [Technical article](https://github.com/stanleyngugi/mathcheck-rl/blob/main/TECHNICAL_ARTICLE.md).

### [MathCheck Engine](https://github.com/stanleyngugi/mathcheck-engine)

The bounded-specification verifier behind MathCheck RL. It builds Lean checks for exact integer results and complete finite pair relations, with explicit verdicts and an opt-in isolated execution path for untrusted input. [Technical article](https://github.com/stanleyngugi/mathcheck-engine/blob/main/TECHNICAL_ARTICLE.md).

### [Formally Verified C](https://github.com/stanleyngugi/formally-verified-code-rl)

A released RL environment for generating C implementations against fixed ACSL contracts, judged by a fail-closed Frama-C WP+RTE pipeline. The public alpha includes a 64-task Core-v1 corpus, proof-replay evidence, negative controls, and an installable Verifiers v1 package. [Technical article](https://github.com/stanleyngugi/formally-verified-code-rl/blob/main/docs/BLOG_POST_DRAFT.md).

## Selected writing

- [Grammars for AI Proof Steps](https://github.com/stanleyngugi/ai-proof-grammars) — two articles and reproducible experiments on grammar-guided Lean tactic generation.
- [Taming Incidental Polysemanticity in Toy Models](https://stanleyngugi.netlify.app/posts/taming_polysemanticity) — a research note on training choices and feature-entanglement proxies in toy networks.

## Earlier research

- [Targeted Lexical Injection](https://arxiv.org/abs/2506.15415) — early-layer LoRA experiments for Swahili–English lexical alignment.
- [Surgical Knowledge Rewrite in Compact LLMs](https://arxiv.org/abs/2508.07075) — an early exploratory study of circuit-localized, two-stage IA³ knowledge editing.

These preprints are part of my earlier research; my present work centers on RL environments and formal verification.

## Writing

I publish research notes and technical essays at [stanleyngugi.netlify.app](https://stanleyngugi.netlify.app/).

Research questions, criticism, and collaboration proposals are welcome through the contact links on my website.
