**Installing JAVA And updating environmental Variable**
- Install java the java from official website -->https://www.java.com/en/download/
- set the  "JAVA_HOME" --> "C:\Program Files\Java\jre1.8.0_201" as environmental variable if it is not set
- add the "%JAVA_HOME%\bin"  to "Path" under System variables

**Download Android SDK and Configure**
- download android sdk command line tool for windows from https://developer.android.com/studio
- "sdk-tools-windows-4333796.zip" unzip this downloaded file and copy to the c folder as "sdk_tools"
- set the path variables as below under system variable

````
"ANDROID_HOME"  --> "C:\sdk-tools"
"Path" --->"%ANDROID_HOME%\platform-tools"
"PAth" --->"%ANDROID_HOME%\tools\bin"
"PAth" --->"%ANDROID_HOME%\tools"

````
- Check the android version
````
C:\Users\hshivanagi>adb --version
Android Debug Bridge version 1.0.41
Version 29.0.5-5949299
Installed as C:\sdk-tools\platform-tools\adb.exe
````

**Install and configure appium server**
- Appium is node package module
- npm is installed with Node.js
- download and Install node js from https://nodejs.org/en/download/
- To download appium issue below command on cmd
````
§npm install -g appium
````




