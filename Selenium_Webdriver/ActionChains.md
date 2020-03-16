**What is Action Chains**
- ActionChains are a ways provided by Selenium to automate low level interactions with websites
- such as mouse movements, mouse button actions, key press, and context menu(right click menu) interactions.
- Using ActionChains object, we call methods that perform specific actions sequentially one by one.
- Actions called are pushed into a queue. 
- When perform() method is called, the events are fired in the order they are queued up.
- The ActionChains implementation is available in below path.
````
from selenium.webdriver.common.action_chains import ActionChains
actionchains = ActionChains(driver) # initialize ActionChain object

menu = driver.find_element_by_id("menu")
submenu = driver.find_element_by_id("submenu1")
ActionChains(driver)
    .move_to_element(menu)
    .click(submenu)
    .perform()

OR
menu = driver.find_element_by_id("menu")
submenu = driver.find_element_by_id("submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(submenu)
actions.perform()
````

**All available actions chain methods**
- click(on_element=None)  -->Left clicks on a given element.
- click_and_hold(on_element=None) -->Click and holds down the left mouse button on an element.
- context_click(on_element=None) -->Performs a context-click (right click) on an element.
- double_click(on_element=None)  -->Double-clicks on an element.
- drag_and_drop(source, target) -->Holds down the left mouse button on the source element, then moves to the target element and releases the mouse button.

````
from_element = driver.find_element_by_id("source")
to_element = driver.find_element_by_id("target")
ActionChains(driver)
    .drag_and_drop(from_element, to_element)
    .perform()

Parameters:
source: The element to mouse down or the element to be dragged
target: The element to mouse up or target element to be dragged into
````

- drag_and_drop_by_offset(source, xoffset, yoffset) -->Holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button.
- key_down(value, element=None) -->Sends a key press only, without releasing it. This is used mainly with modifier keys like Control, Alt and Shift.

````
ActionChains(driver)
    .key_down(Keys.CONTROL)
    .send_keys('c')
    .key_up(Keys.CONTROL)
    .perform()

Parameters
value: The modifier key to send. Keys class defines all values.
element: The element to send keys. If None, sends a key to current focused element.
Example, below script presses ctrl+c
````

- key_up(value, element=None) -->Releases a modifier key.
````
ActionChains(driver)
    .key_down(Keys.CONTROL)
    .send_keys('v')
    .key_up(Keys.CONTROL)
    .perform()

Parameters
value: The modifier key to send. Keys class defines all the values.
element: The element to send keys. If no element passed, sends a key to current focused element.
Example, below script presses ctrl+v
````

- move_by_offset(xoffset, yoffset) -->Moving the mouse to an offset from current mouse position.
- move_to_element(to_element) -->Moving the mouse to the middle of an element. This action helps us to deal with dropdown menu that appears when the user moves the mouse over an element or when the user clicks on an element.

````
menu = driver.find_element_by_id("allmenu")
ActionChains(driver)
    .move_to_element(menu)
    .perform()
# wait until sub menu appears on the screen
WebDriverWait(self.webdriver, 5)
    .until(EC.visibility_of_element_located((By.ID, "home")))
home_menu = driver.find_element_by_id("home")
home_menu.click()

````

- move_to_element_with_offset(to_element, xoffset, yoffset) -->Move the mouse by an offset of the specified element.
Offsets are relative to the top-left corner of the element.

- pause(seconds) -->Pause all actions for the specified duration (in seconds).
- perform() -->Performs all stored actions.
- release(on_element=None) -->Releasing a held mouse button on an element.
- reset_actions() -->To clear all actions already stored locally and/or on the remote end.
- send_keys(keys_to_send) -->Sends keys to current focused element.
- send_keys_to_element(element, keys_to_send) -->Sends keys to an element.