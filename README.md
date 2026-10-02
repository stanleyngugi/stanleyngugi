## Stanley Ngugi

I am a 20-year-old independent self-taught researcher currently focused on post-training via RL, building RL environments, and Formal Verification. I recently dropped out of college to pursue doing research independently.

## Current work

### [Formally Verified C](https://github.com/stanleyngugi/formally-verified-code-rl)

An RL environment where the model is rewarded based on the results of running Frama-C on generated C code, against a fixed input ACSL specification. Verification includes runtime-safety obligations. A full reward is awarded only when all the proofs succeed and some other integrity checks related to keeping the contract fixed pass. Partial rewards are awarded for successful parsing and the fraction of proof obligations discharged. This is currently a public alpha, with 64 tasks available to play with. The judge is isolated, and some adversarial negative controls are used to test whether the judge rejects incorrect implementations. It also produces reproducible proof evidence that can be re-run. Read the [technical article here.](https://stanleyngugi.netlify.app/posts/formally-verified-c.html)

### [MathCheck RL](https://github.com/stanleyngugi/mathcheck-rl)

An RL environment for doing bounded mathematical reasoning, that doesn't rely on answer keys in the primary mode of specification. The model either has to give an integer answer, or a complete finite certificate for the answer. The problem specification is frozen, and a checker in Lean is used to compute reward. Read the [technical article here.](https://stanleyngugi.netlify.app/posts/mathcheck-rl.html)

### [MathCheck Engine](https://github.com/stanleyngugi/mathcheck-engine)

The engine used for MathCheck RL. It is a verification engine that can be used to check answers to bounded mathematical problems. It works by translating the bounded specification into a check that is run in Lean. It can check exact answers, and complete finite relations. It gives reasons for failure, and can be run on untrusted model outputs in an isolated manner. Read the [technical article here.](https://stanleyngugi.netlify.app/posts/mathcheck-engine.html)

## Selected writing

[Grammars for AI Proof Steps](https://github.com/stanleyngugi/ai-proof-grammars): Two articles and some reproducible experiments related to using grammars to guide generation of Lean tactics.

[Taming Incidental Polysemanticity in Toy Models](https://stanleyngugi.netlify.app/posts/taming_polysemanticity): A research note on different training choices and proxies for measuring feature entanglement in toy networks.

## Earlier research

These preprints are from earlier in my research journey. My current focus is on RL environments and formal verification.

[Targeted Lexical Injection](https://arxiv.org/abs/2506.15415): Experiments on doing lexical alignment between Swahili and English via early layer LoRAs.

[Surgical Knowledge Rewrite in Compact LLMs](https://arxiv.org/abs/2508.07075): An early exploration into doing knowledge editing via localizing circuits and using a two stage IA³ approach.

## Writing

I write some research notes and technical essays on my [website.](https://stanleyngugi.netlify.app/)

If you have any questions, criticism, or proposals for research, feel free to contact me via the links on my [website.](https://stanleyngugi.netlify.app/)
