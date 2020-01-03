Procedure to create the andriod virtual device using command line
• download command line tool from below link.
      https://developer.android.com/studio
• From downloaded folder go to the below path
  		C:\Users\hshivanagi\Downloads\sdk-tools\tools\bin
SDK--> software development kit. The sdkmanager is a command line tool that allows you to view, install, update, and uninstall packages for the Android SDK.

commands to install packages
	sdkmanager
	sdkmanager --licenses     # show and offer the option to accept licenses for all available packages that have not already been accepted. 
	sdkmanager --list         # List installed and available packages
	sdkmanager "system-images;android-26;google_apis;x86_64"   
  sdkmanager "platform-tools" "platforms;android-26"         # To install the latest platform tools and the SDK tools for API level 28


