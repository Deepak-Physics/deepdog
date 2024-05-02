{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs";
  inputs.poetry2nixSrc = {
    url = "github:nix-community/poetry2nix";
    inputs.nixpkgs.follows = "nixpkgs";
  };

  outputs = { self, nixpkgs, flake-utils, poetry2nixSrc }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
	poetry2nix = poetry2nixSrc.lib.mkPoetry2Nix { inherit pkgs; };
      in {
        packages = {
	  deepdogApp = poetry2nix.mkPoetryApplication {
            projectDir = self;
	    python = pkgs.python39;
	    preferWheels = true;
	  };
	  deepdogEnv = poetry2nix.mkPoetryEnv {
	    projectDir = self;
	    python = pkgs.python39;
	    preferWheels = true;
	    overrides = poetry2nix.overrides.withDefaults (self: super: {
	    });
	  };
	  default = self.packages.${system}.deepdogEnv;
	};
	devShells.default = pkgs.mkShell {
	  inputsFrom = [ self.packages.${system}.deepdogEnv ];
	  buildInputs = [
	    pkgs.poetry
	    self.packages.${system}.deepdogEnv
	    self.packages.${system}.deepdogApp
	    pkgs.just
	    pkgs.nodejs
	  ];
	  shellHook = ''
	    export DO_NIX_CUSTOM=1
	  '';
	};
      }
    );
}
