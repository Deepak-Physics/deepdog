# Changelog

All notable changes to this project will be documented in this file. See [standard-version](https://github.com/conventional-changelog/standard-version) for commit guidelines.

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
