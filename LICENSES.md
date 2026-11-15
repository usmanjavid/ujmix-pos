# Dependency notices

The project-authored application code and original assets are proprietary (see LICENSE). Product names/domain ownership and branding are not transferred by that code license. Dependencies retain their own copyrights and licenses. The lockfiles pin exact resolved versions; retain upstream notices in any redistributed native bundle.

| Dependency | License |
|---|---|
| Tauri, tauri-build and official plugins | Apache-2.0 OR MIT |
| React / React DOM | MIT |
| TypeScript | Apache-2.0 |
| Vite, Vitest, Tailwind CSS, Zustand, Radix UI, clsx, tailwind-merge | MIT |
| Lucide | ISC |
| Apache ECharts / ZRender | Apache-2.0 / BSD-3-Clause |
| SheetJS Community Edition 0.20.3 (official CDN distribution) | Apache-2.0 |
| Rust standard library | Apache-2.0 OR MIT |
| rusqlite | MIT |
| SQLite | Public domain |
| SQLCipher community edition | BSD-3-Clause |
| OpenSSL (vendored for Windows) | Apache-2.0 |
| serde, serde_json, uuid, chrono | Apache-2.0 OR MIT |
| argon2, rand_core, sha2, hex, base64 | Apache-2.0 OR MIT (check exact package notices) |
| ed25519-dalek | BSD-3-Clause |
| keyring | Apache-2.0 OR MIT |
| tempfile | Apache-2.0 OR MIT |
| Windows SDK/WebView2 runtime | Microsoft terms; not relicensed by this project |

The full 0.2.0 installer redistributes llama.cpp (MIT) and Qwen2.5-0.5B-Instruct Q4_K_M (Apache-2.0), with pinned artifacts and their license/model-card texts in the ai resource directory. Future model weights must have their exact model-card/license/NOTICE and conversion provenance reviewed independently of the inference engine.

`docs/DEPENDENCIES_NODE.json` records package-lock license metadata. `docs/THIRD_PARTY_NOTICES_NODE.txt` includes available installed package license/NOTICE texts. `docs/THIRD_PARTY_NOTICES_RUST.txt` preserves cached Rust dependency license texts (including development/cross-target packages), and both notice files are bundled with the installer. These are useful source-package records, not a completed legal review. Before a commercial native release, generate a complete target-specific Rust and WebView/runtime dependency inventory using cargo metadata/cargo-about and collect all required transitive license texts. Do not infer permissive licensing from a blank metadata field.

Additional 0.2.0 dependencies: ureq (MIT OR Apache-2.0), sysinfo (MIT), tiny_http (MIT OR Apache-2.0, test adapter only), Playwright (Apache-2.0, development/test only). Microsoft redistributable/WebView2 binaries remain governed by Microsoft terms; they are not relicensed under the app's MIT license.

## Web edition

sql.js 1.14.1 (MIT), SQLite (public domain), and the generated SQLite/WebAssembly runtime are bundled only with the browser build. The static package includes THIRD_PARTY_NOTICES_WEB.txt with the sql.js license and frontend dependency notices. Browser cryptography uses the browser's Web Crypto API. No AI model, native llama.cpp runtime, private license issuer key, or server database is part of the web deployment.

BLA (bla-agents) 3.4.1 is used at build time for frontend code protection under the MIT license. Its notice is included in THIRD_PARTY_NOTICES_NODE.txt. Application code and the owner license issuer remain proprietary.
