# Stanley Ngugi

Independent AI researcher working on post-training with reinforcement learning, RL environments, and formal verification.

## Current work

### [Formally Verified C](https://github.com/stanleyngugi/formally-verified-code-rl)

Instead of rewarding C code for passing a test suite, Formally Verified C rewards a model only when Frama-C proves that its implementation satisfies a fixed ACSL specification, including runtime-safety obligations. The public alpha includes 64 tasks, an isolated judge, adversarial negative controls, and reproducible proof evidence. [Technical article](https://stanleyngugi.netlify.app/posts/formally-verified-c.html).

### [MathCheck RL](https://github.com/stanleyngugi/mathcheck-rl)

An RL environment for mathematical reasoning that does not rely on hidden answer keys. Models return an answer or a complete finite certificate, and a frozen problem specification with a Lean-backed checker determines the reward. [Technical article](https://stanleyngugi.netlify.app/posts/mathcheck-rl.html).

### [MathCheck Engine](https://github.com/stanleyngugi/mathcheck-engine)

The verification engine behind MathCheck RL. It turns bounded mathematical specifications into Lean checks for exact answers and complete finite relations, returns explicit failure reasons, and can evaluate untrusted model output in isolation. [Technical article](https://stanleyngugi.netlify.app/posts/mathcheck-engine.html).

## Selected writing

- [Grammars for AI Proof Steps](https://github.com/stanleyngugi/ai-proof-grammars): two articles and reproducible experiments on grammar-guided Lean tactic generation.
- [Taming Incidental Polysemanticity in Toy Models](https://stanleyngugi.netlify.app/posts/taming_polysemanticity): a research note on training choices and feature-entanglement proxies in toy networks.

## Earlier research

- [Targeted Lexical Injection](https://arxiv.org/abs/2506.15415): early-layer LoRA experiments for Swahili–English lexical alignment.
- [Surgical Knowledge Rewrite in Compact LLMs](https://arxiv.org/abs/2508.07075): an early exploratory study of circuit-localized, two-stage IA³ knowledge editing.

These preprints are part of my earlier research; my present work centers on RL environments and formal verification.

## Writing

I publish research notes and technical essays at [stanleyngugi.netlify.app](https://stanleyngugi.netlify.app/).

Research questions, criticism, and collaboration proposals are welcome through the contact links on my website.
