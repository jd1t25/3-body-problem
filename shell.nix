{pkgs ? import <nixpkgs> {}}:
pkgs.mkShell {
  venvDir = "./.venv"; # Directory for the virtual environment

  buildInputs = [
    pkgs.python3
    pkgs.python312Packages.venvShellHook
  ];

  postVenvCreation = ''
    unset SOURCE_DATE_EPOCH
    pip install -U vpython  # Install vpython in the virtual environment
  '';

  shellHook = ''
    echo "Checking for virtual environment..."
    if [ ! -d $venvDir ]; then
      echo "Creating virtual environment..."
      python3 -m venv $venvDir
    else
      echo "Virtual environment already exists."
    fi
    echo "Activate>.."
    source $venvDir/bin/activate
  '';

  postShellHook = ''
    alias sc="source $venvDir/bin/activate"
    export LD_LIBRARY_PATH=${pkgs.zlib}/lib:${pkgs.stdenv.cc.cc.lib}/lib:$LD_LIBRARY_PATH
    export LD_LIBRARY_PATH=${pkgs.lib.makeLibraryPath [
      pkgs.stdenv.cc.cc
    ]}
    export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib/
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath [pkgs.zlib]}:$LD_LIBRARY_PATH"
  '';
}
