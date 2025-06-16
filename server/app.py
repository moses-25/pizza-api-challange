import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from server import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=5555, debug=True)

