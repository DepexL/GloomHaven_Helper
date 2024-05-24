a. What is your application?
The application, named "GloomHaven-Helper", is designed to assist players of the board game GloomHaven. It offers features to manage player progress, create and track characters, and provides a streamlined experience by eliminating the need for physical character sheets.

b. How to run the program?
To run the program, ensure you have Python installed on your system. Then, execute the main script file, which is named appropriately for your operating system (e.g., "main.py" or "main_script.py").

c. How to use the program?
Upon launching the program, users are greeted with a welcoming page where they can choose to start a new game, load an existing progress, or quit the application. Subsequently, they can progress through character creation, player and character management, and saving their game progress. Each step is guided by intuitive UI elements.

2. Body/Analysis

a. Explain how the program covers (implements) functional requirements
The program fulfills several functional requirements:
Player and Character Management: Users can add and remove players, as well as create and delete characters for each player. The program provides interfaces for these operations, ensuring ease of use.
Progress Tracking: Game progress is saved and loaded from a file, allowing users to continue their adventures seamlessly. Additionally, character data such as names and levels are managed effectively.
Leveling System (added functionality): The program implements a leveling system for characters, where users can create characters with specific attributes such as health, mana, stamina, etc. Different character classes are available, each with unique attributes and skills. Users can add skills to characters and manage their progression.

OOP Implamentation:
Polymorphisim:
Overloading:

![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/e244d112-ae66-4075-bd03-61368303b102)

Usage:  Overloading occurs when multiple methods in the same class have the same name but different parameters. This allows each method to customize or extend the behavior of the mothod to suit their specific needs.

 
Usage:  Overriding in my code is used by providing specific implementations of methods (lvl_system and add_skill) in each subclass (Voidwarden_class, Hatchet_class, RedGuard_class, Demolitionist_class) that override the implementations in the superclass (Character_Creator) or subclasses. This allows each subclass to customize or extend the behavior of the inherited methods to suit their specific needs.

Overriding code parts:

![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/c3ceac19-e9f0-48a2-a866-79c823782c1d)

![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/c58bbde7-a833-4609-9d2b-d155b8d6ffd6)

 
 
Abstarction:
Usage: By abstracting the details of button creation into a separate script and class, I promote code organization, modularity, and reusability, which are key benefits of abstraction in software engineering That also include methods that simplify users interaction and so on.
 ![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/7d535875-99e3-4965-aec8-15da0b63b380)


Inheritance:
Usage: Inheritance is utilized to create a hierarchy of classes, where subclasses inherit attributes and methods from a superclass. For instance, subclasses like Voidwarden_class, Hatchet_class, RedGuard_class, and Demolitionist_class inherit from the Character_Creator class, inheriting its attributes and methods.
Superclass:
 ![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/a05e638f-6b04-4a9a-98d1-f10bcc651c8b)


Subclass:
 ![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/77e103f8-d16d-41e0-bcbf-bb87de14272a)

Encapsulation:
Usage: Each class (Character_Creator, Voidwarden_class, Hatchet_class, RedGuard_class, Demolitionist_class) encapsulates related attributes and methods into a cohesive unit representing different character types. The class definition defines the structure and behavior of objects created from that class.
Design Paterns:
Singleton:


Benefits:
Centralized Management: The Singleton ensures that there is only one central point (CharacterManager) responsible for managing character instances.

Global Access: Any part of the application can access the CharacterManager instance to create, retrieve, or manage character instances.

Prevents Duplicate Creation: Ensures that characters with the same name are not created multiple times, preventing duplication.
Singleton code:

![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/c44737b6-a161-4223-98fc-ff6d2bee09c0)


This application of the Singleton pattern provides a centralized and globally accessible way to manage character instances in Character Tracker application.
Decorator:
validate_level decorator checks if the character's level is at least 1 before executing the lvl_system method. If the level is sufficient, the method is executed as usual. Otherwise, a ValueError is raised indicating that the character's level is too low to perform the action.
Decorator code:

 ![image](https://github.com/DepexL/GloomHaven_Helper/assets/166698398/4756001b-948f-45aa-896a-614ccba3afa2)

This, for example, works great because if were to use the level 0 system it would set character health to zero which would be bad.
3. Results and Summary

a. Results (Functional Requirement): The application manages player and character data, allowing users to create, track, and modify game progress but it‘s still not interactble with and isn‘t fully implamented. The leveling system should enhance gameplay by adding depth and customization options for characters.

b. Conclusions (Functional Requirement): The program provides a robust solution for managing GloomHaven game progress, catering to both novice and experienced players. Its intuitive interface and comprehensive features contribute to a smoother gaming experience.

c. Extensibility:

Additional Features: The application could be extended to include more advanced character management features, such as inventory management, character customization options, or interactive character sheets.
Enhanced UI: Improvements in UI design and usability could enhance the overall user experience.
Integration: Integration with online resources or companion apps for GloomHaven could provide additional functionality, such as access to game rules, scenario guides, or community forums.
Overall, the extensibility of the application allows for continuous development and adaptation to meet the evolving needs of GloomHaven players.

