from src.main import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(threaded=True)  # debug=True
