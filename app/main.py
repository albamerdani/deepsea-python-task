from app.controller import reports

deepsea_app = reports.create_app()

if __name__ == "__main__":
    deepsea_app.run(debug=True, port=5000)
