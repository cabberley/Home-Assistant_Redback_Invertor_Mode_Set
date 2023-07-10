# Home Assistant Redback Invertor Mode Set
This repository provides a set of scripts and packages to enable controlling your Redback Technologies Hybrid converter, for best outcomes, you really need to have battery storage attached.

### This is still a work in progress

This package can be setup standalone, however for the best expereince you should firstly install the Redback Technologies Home Assistant Integration first. (https://github.com/juicejuice/homeassistant_redback)

## prerequisites for this install
1. Home Assistant needs pyscript installed and configured
   - Enable "allow all Imports"
   - Enable "Access hass as a global variable?"
2. It will require Home Assistant to store your Redback Portal Username & Password

    Option 1 - use !secrets (example provided in this Repo)
   
   		To use secrets add into your secrets file in your HA config directory
       - redback_email: <your email portal account address>
       - redback_password: <your redback portal account password>
   
     	In your Home assistant configuration.yaml file
   
       - add a pyscript: section if one doesn't already exist and add the following YAML
         pyscript:
           secrets: 
             redback_email: !secret redback_email
             redback_password: !secret redback_password
   Option 2 - edit the script after it has been setup in Home Assistant

   		replace the email: secret with 'email: your email address'
     	replace the password: secret with 'password: your password'

3. If you aren't using the Redback Technologies Home Assistant Integration you will need to log into your Redback Portal website and collect the following information.
   - Inverter number: RB201XXXXXXXX from the Details page.
   - EMS Firwamre: 2.17.xxx.x from the "view current settings" from the Settings page.

## Installing the pyscript
1. If you haven't already installed pyscript, information to install this HACS integration can be found here: [Home Assistant - Pyscript](https://hacs-pyscript.readthedocs.io/en/stable/)
2. In your Home Assistant - pyscript folder copy the contents of this repositories pyscript folders.


## Installing the package
1. If it doesn't exist already create a folder called 'packages' under your home assistant config directory see here for details about the [Home Assistant Packages](https://www.home-assistant.io/docs/configuration/packages/#:~:text=Packages%20in%20Home%20Assistant%20provide%20a%20way%20to,the%20%21include%20directives%20introduced%20in%20splitting%20the%20configuration).
2. Copy the folder and yaml file from the packages folder in this repository, to the packages folder on your Home Assistant. You will need to edit the "redback_inverter_mode.yaml file and update the following two lines, update the entity to reflect the name you gavce your Redback Technologies integration :
   serialNumber: "{{ state_attr( \"sensor.redback_inverter_status\",\"serial_number\") }}"
   swVersion: "{{ state_attr( \"sensor.redback_inverter_status\",\"software_version\") }}"
3. If you do not have the Redback Technologies Home Assistant Integration installed you will need to edit the script file as well.
   - replace the value for serialNumber: with your Inverter number
   - replace the swVersion: with your EMS Firmware value
5. Restart your Home assitant to load the contents of the packages.

## Using the Integration
1. After completing the setup and restarting your Home Assistant you should now have the capabiltiy to control your Redback Hybriod Inverter from HA.
2. You should now have in your Helpers
   - input_number: redback_inverter_power_setting_w
   - input_select: redback_inverter_mode_Setting
   - input_button: redback_inverter_set_mode
3. Under Automation\scripts a new script called "Redback Inverter Mode Update"
4. On one of your dashboards add a Card and use the "Manual" template, Copy and paste the content from "card_template.yaml" in this repository.
   - If you do not have the redback integration installed the first card in the stack will not display anything and may show errors that it can't find the entities, you may have to delete this section from your card.

## To test your install
1. Change the mode and power settings on the dashboard and press the button.
2. Wait about 60-90 seconds, as the inverter normally only updates once every 60 seconds.
3. Check in your Redback Portal on the "settings" page if the Inverter Section at the bottom reflects the settings you sent.
   
NOTE: in "Auto" mode it will ignore any Power number that is submitted.
  
NOTE: I normally only use "Auto", "Charge Battery" & "Discharge Battery"
   
NOTE: The inverter will stay in this mode until you either make a change in your HA Dashboard or through the Redback Portal.
   
