from project import create_app

app = create_app()

if __name__=='__main__':
    port = int(os.getenv('PORT',5000))
    app.run(host="0.0.0.0", debug=True, port=port)