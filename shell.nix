{ pkgs ? import (fetchTarball "https://github.com/NixOS/nixpkgs/tarball/nixos-23.05") {} }:

pkgs.mkShell {
    packages = with pkgs; [
        git
        vim
        pipreqs
        (python3.withPackages (p : [
          p.docopt
          p.inquirerpy
          p.pyyaml
          p.textual
          p.pip
        ]))
    ];
}