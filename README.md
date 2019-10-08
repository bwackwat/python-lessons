# python-lessons

Lessons and documentation for learning about Object Oriented Python programming and testing techniques.

## Lesson 1: Modularization and basic testing

Contained in the modules/ directory.

* Notice the unique ways to import.
  * Namespace (module) imports are on the same level as the executing file.
  * Regular (module) imports execute the `__init__.py` file of a subdirectory relative to the directory the executing file is in.
  * Using a cool hack, we can support regular imports and regular imports from the parent directory.
 
