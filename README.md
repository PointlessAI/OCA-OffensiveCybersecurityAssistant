# OCA - Offensive Cybersecurity Assistant
# ChatGPT API Terminal Assistant with a good memory to be used in ethical hacking
**Warning:** These scripts are for training purposes to accompany a training course. Do not use on real applications without explicit permissions.
## To run, clone then cd to dir, then execute main.py
## Run [T]erminal commands using 't' or [G]eneral chat using 'g' or [C]onsultant using 'c'
## In terminal: export OPENAI_API_KEY=[OPENAI API KEY]
* Requires Python + Openai + ChatGPT API key

**Warning:** These scripts are under development and may contain bugs or security issues. Please use responsibly.

# Workflow

![ChatGPT Terminal Assistant](https://github.com/PointlessAI/ChatGPT-TerminalAssistant/blob/main/Img/workflow.png)

## 1. General Assistant for High-Level Learning of Ethical Hacking
Utilize the general assistant to gain a high-level understanding of ethical hacking concepts. This phase focuses on foundational knowledge and broad insights into ethical hacking practices.

## 2. Red Team Assistant for Detailed Consultation on Offensive Security Methods
Engage the red team assistant for in-depth consultations regarding offensive security methods. This step involves acquiring detailed insights and strategic guidance to enhance offensive security skills.

## 3. Terminal Assistant to Execute Attacks - STRICTLY FOR THE PURPOSE OF LEARNING.
**Warning:** These scripts are for training purposes to accompany a training course. Do not use on real applications without explicit permissions.
Leverage the terminal assistant for hands-on experience in executing ethical hacking attacks. This phase involves practical application, allowing you to implement the learned concepts in a real-world environment.

* Switching between assistants.
![ChatGPT Terminal Assistant](https://github.com/PointlessAI/ChatGPT-TerminalAssistant/blob/main/Img/assistants.png)

**Warning:** Ensure that ethical hacking practices are conducted responsibly and legally, adhering to ethical standards and applicable laws.

# Video
[![Video Title](https://img.youtube.com/vi/ZIfdgZcxkRg/maxresdefault.jpg)](https://youtu.be/ZIfdgZcxkRg)

# Screenshots
* Network & vulnerability scanning
![ChatGPT Terminal Assistant](https://github.com/PointlessAI/ChatGPT-TerminalAssistant/blob/main/Img/nikto.png)
* Brute forcing
![ChatGPT Terminal Assistant](https://github.com/PointlessAI/ChatGPT-TerminalAssistant/blob/main/Img/hydra.png)
* SQL injection
![ChatGPT Terminal Assistant](https://github.com/PointlessAI/ChatGPT-TerminalAssistant/blob/main/Img/sqlinjection.png)

# Bug reporting
**Contact@pointlessai.com**

# Example of Red Team [C]onsultant output:

# Your request Sire?: how to use selenium

*Patience, my Lord, we will find the answers you seek....*

1. **Short Answer**: Install Selenium WebDriver and a programming language binding (e.g., Python), then write a script to control a web browser programmatically.

2. **Reasoning**: Selenium WebDriver is a tool for automating web browser interaction, allowing you to perform tasks such as navigating to a web page, filling out forms, and extracting data programmatically. It supports multiple programming languages and browsers, making it versatile for web automation and testing tasks.

3. **Sources**: The official Selenium documentation ([https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)) provides comprehensive guides, API references, and tutorials for getting started and advancing with Selenium WebDriver.

4. **How to Use This Offensively**: In an offensive context, Selenium can be used for automating exploitation tasks such as credential stuffing, automated scanning of web applications for vulnerabilities, or simulating user actions to bypass client-side security controls.

5. **How to Defend Against This**: Implementing CAPTCHA, account lockout mechanisms, and detecting unusual user behavior can help mitigate automated attacks using tools like Selenium. Employing Content Security Policy (CSP) can also reduce the risk of certain client-side attacks.

6. **Secret Answer**: Selenium can be used in headless mode, where the browser does not display a UI, making automation tasks faster and less resource-intensive. This mode is particularly useful for running tests or automation scripts on servers or in environments where a graphical user interface is not necessary.

7. **Alternative View**: While Selenium is powerful for web automation, it can be detected by sophisticated websites that implement bot detection mechanisms. Alternatives like Puppeteer, which controls headless Chrome or Chromium, might be less detectable in some cases.

8. **Red Team Expert Suggestions**: When using Selenium for red teaming, consider rotating user agents and using proxy servers to mimic real user behavior and avoid detection. Also, leverage Selenium's ability to execute JavaScript to test for XSS vulnerabilities or to perform actions that require client-side scripting. Always ensure your actions are authorized and ethical.

9. **Raw Shell Command**: Assuming you're using Python, first ensure you have Python and pip installed, then install Selenium using pip:
   ```bash
   pip install selenium

Then, you can write a simple script to open a browser and navigate to a webpage:

```python
from selenium import webdriver

driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
driver.get("http://www.example.com")


