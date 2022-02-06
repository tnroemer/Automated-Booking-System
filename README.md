# Automated Booking System
 Allows you to automatically sign up to meals at Nuffield College.

# Dependencies

To be able to run the script you need to install the required dependencies in your virtual environment. Do this by running:

`pip install selenium`

`pip install regex`

`pip install tqdm`

in the command line.

The script runs by sending requests via a browser to the booking system. To do this it uses the chrome driver. To be able to work you need to have installed Chrome (v98) and download the Chrome driver, which you can get from [here](https://chromedriver.storage.googleapis.com/index.html?path=98.0.4758.80/). Create a folder called 'driver' in the same directory as the `Automatic_Booking_System.py` file and place the chromedriver in there. Double click on the chromedriver file and press `open` when asked whether you want to open it. We need to do this to allow the script to open the file later. After you clicked `open` in the dialog you can close the terminal window that opens.

# Usage

 To use the booking system script open the command line, type `python3` and drag the file `Automated_Booking_System.py` file into the terminal. Your command line should look like this: `python3 /Users/YourName/.../Automated_Booking_System.py`, where the `...` depend on where you saved the file. Press enter and follow the instructions. Note that the command line does not indicate whether you typed anything when typing in the password. That does not mean the input is not read, however.
 
 The script will iterate over all booking forms you wish to sign up for, filling in your dietary requirements on the go. Your command line should look similar to this:
<p align="center">
    <img src="images/example.png" width="650">
<p>

 # Bugs
 
  The Chrome driver together with Selenium (which we use to send the requests) has a bug which does not allow you to pass strings with special characters to the driver. This means that your password cannot contain any of those for the script to run through. You can follow the debugging status [here](https://github.com/SeleniumHQ/selenium/issues/10318).
