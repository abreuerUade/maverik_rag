

if (!(Test-Path -Path "python")) {
    New-Item -ItemType Directory -Path "python"
}

pip install -r requirements.txt -t python/

Compress-Archive -Path "python" -DestinationPath layer.zip -Force

Compress-Archive -Path "src" -DestinationPath src.zip -Force

