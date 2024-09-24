import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QTextEdit, QPushButton, QFileDialog, QMessageBox, QTabWidget, QFormLayout
)
from PyQt5.QtGui import QIcon

class ReadmeGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Readme Pro")
        self.setGeometry(100, 100, 800, 600)
        
        # Set window icon
        self.setFixedSize(800,600)
        self.setWindowIcon(QIcon("icons/Readme Pro.png"))

        self.init_ui()
        self.projects = []

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.info_tab = QWidget()
        self.skills_tab = QWidget()
        self.projects_tab = QWidget()

        self.tab_widget.addTab(self.info_tab, "Info")
        self.tab_widget.addTab(self.skills_tab, "Skills")
        self.tab_widget.addTab(self.projects_tab, "Projects")

        self.init_info_tab()
        self.init_skills_tab()
        self.init_projects_tab()

        self.readme_preview = QTextEdit()
        self.layout.addWidget(self.readme_preview)

        # Create toolbar
        self.create_toolbar()

        self.generate_button = QPushButton("Generate README")
        self.generate_button.setIcon(QIcon("icons/generate.png"))  # Set icon for generate button
        self.generate_button.clicked.connect(self.generate_readme)
        self.layout.addWidget(self.generate_button)

        self.save_button = QPushButton("Save README")
        self.save_button.setIcon(QIcon("icons/save.png"))  # Set icon for save button
        self.save_button.clicked.connect(self.save_readme)
        self.layout.addWidget(self.save_button)

    def create_toolbar(self):
        toolbar = self.addToolBar("Toolbar")
        toolbar.setMovable(False)

        new_action = toolbar.addAction(QIcon("icons/new.png"), "New")
        new_action.triggered.connect(self.clear_inputs)

        # You can add more actions/buttons here as needed

    def clear_inputs(self):
        # Clear all inputs when 'New' is clicked
        self.name_input.clear()
        self.bio_input.clear()
        self.profile_image_input.clear()
        self.skills_input.clear()
        self.skill_level_input.clear()
        self.github_input.clear()
        self.twitter_input.clear()
        self.linkedin_input.clear()
        self.instagram_input.clear()
        self.youtube_input.clear()
        self.facebook_input.clear()
        self.website_input.clear()
        self.project_input.clear()
        self.project_tags_input.clear()
        self.projects.clear()
        self.projects_list.clear()
        self.readme_preview.clear()

    def init_info_tab(self):
        layout = QFormLayout()

        self.name_input = QLineEdit()
        layout.addRow("Name:", self.name_input)

        self.bio_input = QTextEdit()
        layout.addRow("Bio:", self.bio_input)

        # Keep the input for profile image as a URL
        self.profile_image_input = QLineEdit()
        layout.addRow("Profile Image URL:", self.profile_image_input)

        self.info_tab.setLayout(layout)

    def init_skills_tab(self):
        layout = QFormLayout()

        self.skills_input = QLineEdit()
        layout.addRow("Skills (comma separated):", self.skills_input)

        self.skill_level_input = QLineEdit()
        layout.addRow("Skill Levels (comma separated):", self.skill_level_input)

        self.github_input = QLineEdit()
        layout.addRow("GitHub URL:", self.github_input)

        self.twitter_input = QLineEdit()
        layout.addRow("Twitter URL:", self.twitter_input)

        self.linkedin_input = QLineEdit()
        layout.addRow("LinkedIn URL:", self.linkedin_input)

        self.instagram_input = QLineEdit()
        layout.addRow("Instagram URL:", self.instagram_input)

        self.youtube_input = QLineEdit()
        layout.addRow("YouTube URL:", self.youtube_input)

        self.facebook_input = QLineEdit()
        layout.addRow("Facebook URL:", self.facebook_input)

        self.website_input = QLineEdit()
        layout.addRow("Website URL:", self.website_input)

        self.skills_tab.setLayout(layout)

    def init_projects_tab(self):
        layout = QVBoxLayout()

        self.project_input = QLineEdit()
        layout.addWidget(QLabel("Project Name:"))
        layout.addWidget(self.project_input)

        self.project_tags_input = QLineEdit()
        layout.addWidget(QLabel("Project Tags (comma separated):"))
        layout.addWidget(self.project_tags_input)

        self.add_project_button = QPushButton("Add Project")
        self.add_project_button.setIcon(QIcon("icons/project.png"))  # Set icon for generate button
        self.add_project_button.clicked.connect(self.add_project)
        layout.addWidget(self.add_project_button)

        self.projects_list = QTextEdit()
        self.projects_list.setReadOnly(True)
        layout.addWidget(self.projects_list)

        self.projects_tab.setLayout(layout)

    def add_project(self):
        project = self.project_input.text()
        tags = self.project_tags_input.text()
        if project:
            project_entry = f"{project} [{tags}]"
            self.projects.append(project_entry)
            self.projects_list.append(project_entry)
            self.project_input.clear()
            self.project_tags_input.clear()
        else:
            QMessageBox.warning(self, "Input Error", "Please enter a project name.")

    def generate_readme(self):
        name = self.name_input.text()
        bio = self.bio_input.toPlainText()
        profile_image_url = self.profile_image_input.text()
        skills = self.skills_input.text().split(',')
        skill_levels = self.skill_level_input.text().split(',')
        github_url = self.github_input.text()
        twitter_url = self.twitter_input.text()
        linkedin_url = self.linkedin_input.text()
        instagram_url = self.instagram_input.text()
        youtube_url = self.youtube_input.text()
        facebook_url = self.facebook_input.text()
        website_url = self.website_input.text()

        readme_content = f"# {name}  \n"
        if profile_image_url:
            readme_content += f"![Profile Image]({profile_image_url})  \n"
        readme_content += f"{bio}\n\n## Skills\n"

        for skill, level in zip(skills, skill_levels):
            badge = f"![{skill.strip()}](https://img.shields.io/badge/{skill.strip()}-{level.strip()}-blue)"
            readme_content += f"{badge}\n"

        readme_content += "\n## Projects\n" + "\n".join(self.projects) + "\n"

        readme_content += "## Social Links\n"
        if github_url:
            readme_content += f"- [GitHub]({github_url}) ![GitHub](https://img.shields.io/badge/GitHub-000000?style=flat&logo=github)\n"
        if twitter_url:
            readme_content += f"- [Twitter]({twitter_url}) ![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=flat&logo=twitter)\n"
        if linkedin_url:
            readme_content += f"- [LinkedIn]({linkedin_url}) ![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)\n"
        if instagram_url:
            readme_content += f"- [Instagram]({instagram_url}) ![Instagram](https://img.shields.io/badge/Instagram-E1306C?style=flat&logo=instagram)\n"
        if youtube_url:
            readme_content += f"- [YouTube]({youtube_url}) ![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube)\n"
        if facebook_url:
            readme_content += f"- [Facebook]({facebook_url}) ![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=flat&logo=facebook)\n"
        if website_url:
            readme_content += f"- [Website]({website_url}) ![Website](https://img.shields.io/badge/Website-000000?style=flat&logo=web)\n"

        self.readme_preview.setPlainText(readme_content)

    def save_readme(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save README File", "", "Markdown Files (*.md);;All Files (*)", options=options)
        if file_name:
            with open(file_name, 'w') as file:
                file.write(self.readme_preview.toPlainText())
                QMessageBox.information(self, "Success", "README saved successfully!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ReadmeGenerator()
    window.show()
    sys.exit(app.exec_())
