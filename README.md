[README.md](https://github.com/user-attachments/files/21727545/README.md)
# AI Co-Professor

AI Co-Professor is an intelligent assistant designed to evaluate students' Group Discussion (GD) performance and provide instant feedback based on leadership potential, domain knowledge, communication skills, and teamwork. It integrates seamlessly with Microsoft Teams and is hosted on Azure App Service.

## Features

- Audio/video GD session upload and processing
- Speech-to-text transcription and speaker identification
- NLP-based scoring engine
- Feedback report generation
- Professor and student dashboards
- Microsoft Teams tab integration
- Azure App Service hosting

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/<your-username>/AI-Co-Professor.git
   cd AI-Co-Professor

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app locally:
   uvicorn app:app --reload

## Azure App Service Deployment

1. Zip the project folder including:
   - app.py
   - AI_Co_Professor_Dashboard.html
   - requirements.txt

2. Go to Azure Portal > Create Web App

3. Choose runtime (Python 3.10), region, and deployment method (Zip Deploy)

4. Upload the ZIP file via Deployment Center

5. Access your app at https://<your-app-name>.azurewebsites.net

## Microsoft Teams Integration

1. Update manifest.json with your Azure-hosted URL

2. Package the manifest with icons into a ZIP

3. Go to Teams > Apps > Upload a custom app

4. Select your team and upload the ZIP

5. Access the dashboard via the Teams tab

## Contribution Guidelines

- Fork the repository
- Create a feature branch
- Commit your changes with clear messages
- Submit a pull request

## License

This project is licensed under the MIT License.
