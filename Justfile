download number:
    bash download.sh {{number}}

python number:
    #!/bin/bash
    filepath=$(find . -type f -name "{{number}}.py")
    uv run $filepath

