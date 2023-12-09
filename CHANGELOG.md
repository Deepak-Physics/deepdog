# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

### [0.7.5](https://gitea.deepak.science:2222/physics/deepdog/compare/0.7.4...0.7.5) (2023-12-09)


### Features

* adds direct monte carlo package ([1741807](https://gitea.deepak.science:2222/physics/deepdog/commit/1741807be43d08fb51bc94518dd3b67585c04c20))
* adds longchain logging if logging last generation ([b4e5f53](https://gitea.deepak.science:2222/physics/deepdog/commit/b4e5f5372682fc64c3734a96c4a899e018f127ce))
* allows disabling timestamp in subset simulation bayes results ([9a4548d](https://gitea.deepak.science:2222/physics/deepdog/commit/9a4548def45a01f1f518135d4237c3dc09dcc342))

### [0.7.4](https://gitea.deepak.science:2222/physics/deepdog/compare/0.7.3...0.7.4) (2023-07-27)


### Features

* adds configurable chunk size for the initial mc level 0 SS stage cost calculation to reduce memory usage ([9a7a3ff](https://gitea.deepak.science:2222/physics/deepdog/commit/9a7a3ff2c7ebe81d5e10647ce39844c372ff7b07))
* allows for deepdog bayesrun with ss to not print csv to make snapshot testing possible ([8e6ead4](https://gitea.deepak.science:2222/physics/deepdog/commit/8e6ead416c9eba56f568f648d0df44caaa510cfe))


### Bug Fixes

* fixes bug if case of clamping necessary ([161bcf4](https://gitea.deepak.science:2222/physics/deepdog/commit/161bcf42addf331661c3929073688b9f2c13502c))
* fixes bug with clamped probabilities being underestimated ([e6defc7](https://gitea.deepak.science:2222/physics/deepdog/commit/e6defc794871a48ac331023eb477bd235b78d6d0))

### [0.7.3](https://gitea.deepak.science:2222/physics/deepdog/compare/0.7.2...0.7.3) (2023-07-27)


### Features

* adds utility options and avoids memory leak ([598dad1](https://gitea.deepak.science:2222/physics/deepdog/commit/598dad1e6dc8fc0b7a5b4a90c8e17bf744e8d98c))

### [0.7.2](https://gitea.deepak.science:2222/physics/deepdog/compare/0.7.1...0.7.2) (2023-07-24)


### Features

* clamps results now ([9bb8fc5](https://gitea.deepak.science:2222/physics/deepdog/commit/9bb8fc50fe1bd1a285a333c5a396bfb6ac3176cf))


### Bug Fixes

* fixes clamping format etc. ([a170a3c](https://gitea.deepak.science:2222/physics/deepdog/commit/a170a3ce01adcec356e5aaab9abcc0ec4accd64b))

### [0.7.1](https://gitea.deepak.science:2222/physics/deepdog/compare/0.7.0...0.7.1) (2023-07-24)


### Features

* adds subset simulation stuff ([33cab9a](https://gitea.deepak.science:2222/physics/deepdog/commit/33cab9ab4179cec13ae9e591a8ffc32df4dda989))

## [0.7.0](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.7...0.7.0) (2023-05-01)


### ⚠ BREAKING CHANGES

* removes fastfilter parameter because it should never be needed

### Features

* adds pair capability to real spectrum run hopefully ([a089951](https://gitea.deepak.science:2222/physics/deepdog/commit/a089951bbefcd8a0b2efeb49b7a8090412cbb23d))
* removes fastfilter parameter because it should never be needed ([a015daf](https://gitea.deepak.science:2222/physics/deepdog/commit/a015daf5ff6fa5f6155c8d7e02981b588840a5b0))

### [0.6.7](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.6...0.6.7) (2023-04-14)


### Features

* adds option to cap core count for real spectrum run ([bf15f4a](https://gitea.deepak.science:2222/physics/deepdog/commit/bf15f4a7b7f59504983624e7d512ed7474372032))
* adds option to cap core count for temp aware run ([12903b2](https://gitea.deepak.science:2222/physics/deepdog/commit/12903b2540cefb040174d230bc0d04719a6dc1b7))


### Bug Fixes

* avoids redefinition of core count in loop ([1cf4454](https://gitea.deepak.science:2222/physics/deepdog/commit/1cf44541531541088198bd4599d467df3e1acbcf))

### [0.6.6](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.5...0.6.6) (2023-04-09)


### Bug Fixes

* removes bad logging in multiprocessing function ([8fd1b75](https://gitea.deepak.science:2222/physics/deepdog/commit/8fd1b75e1378301210bfa8f14dd09174bbd21414))

### [0.6.5](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.4...0.6.5) (2023-04-09)


### Features

* adds temp aware guy using new pdme temp-flexible feature for bundling temp models ([de1ec3e](https://gitea.deepak.science:2222/physics/deepdog/commit/de1ec3e70062d418e0d4c89716905cc9313d2e26))

### [0.6.4](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.3...0.6.4) (2022-08-13)


### Features

* Prints model names while running ([7ea1d71](https://gitea.deepak.science:2222/physics/deepdog/commit/7ea1d715f67e81c9fa841c5a62f1cc700ff7363d))

### [0.6.3](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.2...0.6.3) (2022-06-12)


### Features

* adds fast filter variant ([2c5c122](https://gitea.deepak.science:2222/physics/deepdog/commit/2c5c1228209e51d17253f07470e2f1e6dc6872d7))
* adds tester for fast filter real spectrum ([0a1a277](https://gitea.deepak.science:2222/physics/deepdog/commit/0a1a27759b0d4ab01da214b76ab14bf2b1fe00e3))

### [0.6.2](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.1...0.6.2) (2022-05-26)


### Features

* adds better import api for real data run ([d7e0f13](https://gitea.deepak.science:2222/physics/deepdog/commit/d7e0f13ca55197b24cb534c80f321ee76b9c4a40))

### [0.6.1](https://gitea.deepak.science:2222/physics/deepdog/compare/0.6.0...0.6.1) (2022-05-22)


### Features

* adds new runner for real spectra ([bd56f24](https://gitea.deepak.science:2222/physics/deepdog/commit/bd56f247748babb2ee1f2a1182d25aa968bff5a5))

## [0.6.0](https://gitea.deepak.science:2222/physics/deepdog/compare/0.5.0...0.6.0) (2022-05-22)


### ⚠ BREAKING CHANGES

* bayes run now handles multidipoles with changes to output file format etc.
* logs multiple dipoles better maybe
* switches over to pdme new stuff, uses models and scraps discretisations entirely
* removes alt_bayes bayes distinction, which was superfluous when only alt worked

### Features

* adds pdme 0.7.0 for multiprocessing ([874d876](https://gitea.deepak.science:2222/physics/deepdog/commit/874d876c9d774433b034d47c4cc0cdac41e6f2c7))
* bayes run now handles multidipoles with changes to output file format etc. ([5d0a7a4](https://gitea.deepak.science:2222/physics/deepdog/commit/5d0a7a4be09c58f8f8f859384f01d7912a98b8b9))
* logs multiple dipoles better maybe ([ae8977b](https://gitea.deepak.science:2222/physics/deepdog/commit/ae8977bb1e4d6cd71e88ea0876da8f4318e030b6))
* removes alt_bayes bayes distinction, which was superfluous when only alt worked ([101569d](https://gitea.deepak.science:2222/physics/deepdog/commit/101569d749e4f3f1842886aa2fd3321b8132278b))
* switches over to pdme new stuff, uses models and scraps discretisations entirely ([6e29f7a](https://gitea.deepak.science:2222/physics/deepdog/commit/6e29f7a702b578c266a42bba23ac973d155ada10))
* Uses multidipole for bayes run, with more verbose output ([df89776](https://gitea.deepak.science:2222/physics/deepdog/commit/df8977655de977fd3c4f7383dd9571e551eb1382))


### Bug Fixes

* another bug fix for csv generation ([b7da3d6](https://gitea.deepak.science:2222/physics/deepdog/commit/b7da3d61cc5c128cba1d2fcb3770b71b7f6fc4b8))
* fixes crash when dipole count is smaller than expected max during file write ([b5e0ecb](https://gitea.deepak.science:2222/physics/deepdog/commit/b5e0ecb52886b32d9055302eacfabb69338026b4))
* fixes format string in csv output for headers ([9afa209](https://gitea.deepak.science:2222/physics/deepdog/commit/9afa209864cdb9255988778e987fe05952848fd4))
* fixes random issue ([eec926a](https://gitea.deepak.science:2222/physics/deepdog/commit/eec926aaac654f78942b4c6b612e4d1cdcbf81dc))
* moves logging successes to after they've actually happened ([0caad05](https://gitea.deepak.science:2222/physics/deepdog/commit/0caad05e3cc6a9adba8bf937c3d2f944e1b096a3))
* now doesn't double randomise frequency ([23b202b](https://gitea.deepak.science:2222/physics/deepdog/commit/23b202beb81cb89f7f20b691e83116fa53764902))
* whoops deleted word multiprocessing ([31070b5](https://gitea.deepak.science:2222/physics/deepdog/commit/31070b5342c265d930b4c51402f42a3ee2415066))

## [0.5.0](https://gitea.deepak.science:2222/physics/deepdog/compare/0.4.0...0.5.0) (2022-04-30)


### ⚠ BREAKING CHANGES

* simulpairs now uses different rng calculator

### Features

* adds simulpairs run ([e9277c3](https://gitea.deepak.science:2222/physics/deepdog/commit/e9277c3da777359feb352c0b19f3bb029248ba2f))
* has better parallelisation ([edf0ba6](https://gitea.deepak.science:2222/physics/deepdog/commit/edf0ba6532c0588fce32341709cdb70e384b83f4))
* simulpairs now uses different rng calculator ([50dbc48](https://gitea.deepak.science:2222/physics/deepdog/commit/50dbc4835e60bace9e9b4ba37415f073a3c9e479))


### Bug Fixes

* better parallelisation hopefully ([42829c0](https://gitea.deepak.science:2222/physics/deepdog/commit/42829c0327e080e18be2fb75e746f6ac0d7c2f6d))
* Makes altbayessimulpairs available in package ([492a5e6](https://gitea.deepak.science:2222/physics/deepdog/commit/492a5e6681c85f95840e28cfd5d4ce4ca1d54eba))
* stronger names ([0954429](https://gitea.deepak.science:2222/physics/deepdog/commit/0954429e2d015a105ff16dfbb9e7a352bf53e5e9))
* Uses correct filename arg for passed in rng ([349341b](https://gitea.deepak.science:2222/physics/deepdog/commit/349341b405375a43b933f1fd7db4ee9fc501def3))
* uses correct filename for pairs guy ([4c06b39](https://gitea.deepak.science:2222/physics/deepdog/commit/4c06b3912c811c93c310b1d9e4c153f2014c4f8b))

## [0.4.0](https://gitea.deepak.science:2222/physics/deepdog/compare/0.3.5...0.4.0) (2022-04-10)


### ⚠ BREAKING CHANGES

* Adds pair calculations, with changing api format

### Features

* Adds dynamic cycle count increases to help reach minimum success count ([ec7b4ca](https://gitea.deepak.science:2222/physics/deepdog/commit/ec7b4cac393c15e94c513215c4f1ba32be2ae87a))
* Adds pair calculations, with changing api format ([6463b13](https://gitea.deepak.science:2222/physics/deepdog/commit/6463b135ef2d212b565864b5ac1b655e014d2194))


### Bug Fixes

* uses bigfix from pdme for negatives ([c1c711f](https://gitea.deepak.science:2222/physics/deepdog/commit/c1c711f47b574d3a9b8a24dbcbdd7f50b9be8ea9))

### [0.3.5](https://gitea.deepak.science:2222/physics/deepdog/compare/0.3.4...0.3.5) (2022-03-07)


### Features

* makes chunksize configurable ([88d9613](https://gitea.deepak.science:2222/physics/deepdog/commit/88d961313c1db0d49fd96939aa725a8706fa0412))

### [0.3.4](https://gitea.deepak.science:2222/physics/deepdog/compare/0.3.3...0.3.4) (2022-03-06)


### Features

* Changes chunksize for multiprocessing ([0784cd5](https://gitea.deepak.science:2222/physics/deepdog/commit/0784cd53d79e00684506604f094b5d820b3994d4))

### [0.3.3](https://gitea.deepak.science:2222/physics/deepdog/compare/0.3.2...0.3.3) (2022-03-06)


### Bug Fixes

* Fixes count to use cycles as well ([8617e4d](https://gitea.deepak.science:2222/physics/deepdog/commit/8617e4d2742b112cc824068150682ce3b2cdd879))

### [0.3.2](https://gitea.deepak.science:2222/physics/deepdog/compare/0.3.1...0.3.2) (2022-03-06)


### Features

* Adds monte carlo cycles to trade off space and cpu ([e6d8d33](https://gitea.deepak.science:2222/physics/deepdog/commit/e6d8d33c27e7922581e91c10de4f5faff2a51f8b))

### [0.3.1](https://gitea.deepak.science:2222/physics/deepdog/compare/v0.3.0...v0.3.1) (2022-03-06)


### Features

* Adds alt bayes solver with monte carlo sampler ([7284dbe](https://gitea.deepak.science:2222/physics/deepdog/commit/7284dbeb34ef46189d81fb719252dfa74b8e9fa8))
* Updates to pdme version for faster bayes resolution ([d078004](https://gitea.deepak.science:2222/physics/deepdog/commit/d078004773d9d9dccd0a9a52ca96aa57690f9b7e))
