## Code for calling the owner of this PiPatrol. This part integrates with an IFTTT Maker Event applet.

# define trigger URL
url = <INSERT_URL_GIVEN_BY_IFTTT_HERE>

# path to the web browser
chrome_path = '/usr/lib/chromium-browser/chromium-browser'
    
# command to open URL in browser
webbrowser.get(chrome_path).open(url)
