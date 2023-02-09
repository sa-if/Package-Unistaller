<h1 align="center">Package Uninstaller.✌️👍</h1>


` A python script to Uninstall all python packages at once.🙂
`
## Work Model 🤩
 - Creates a file named `requirements.txt` and writes the output of the `pip freeze` command to it. The `pip freeze` command lists all the packages that are currently     installed in your Python environment and their versions.
 - Reads the contents of the `requirements.txt` file, which contains the list of packages and their versions, and splits them into a list of strings, where each           string is a package name and version.    
 - Loops through the list of packages and uninstalls each one using the `pip uninstall` command. The `-y` option is used to answer "yes" to any prompts asking to         confirm the uninstallation.
 
      This code can be used to create a snapshot of the currently installed packages in a Python environment and then to uninstall all of those packages at once. This       can be useful for scenarios where you want to start with a clean slate and have no installed packages, or when you want to ensure that you are only using the           packages that are explicitly listed in the `requirements.txt` file.
 

 
 
 ## Prerequisites 🤖
You need to have the following software installed on your machine:
- `Python 3.x`
- `pip`
- `Required packages`
- `Permission`


## Usage 🎃
- To use this script, simply run the following command: `python main.py`

## Error handling
  -  The script includes error handling for both the creation of the `requirements.txt` file and the uninstallation of packages. In case of any errors, the error            message will be printed to the console.

## License 🪪
The project is licensed under MIT license. See the `license` file for details.

## Authors 👦🏻

- [@saifislam](https://www.github.com/sa-if)


## Used By 🧑‍🤝‍🧑

This project is used by the following individual:

- `Saif Islam`  
- `Saimoon Islam`

## Contributions

Feel free to contribute to this project by opening an issue or submitting a pull request.


## Support 💁🏻‍♂️

For support, email `saifislam23122005@gmail.com` or join `facebook` community.(●'◡'●)







