import sys

mode = input("Choose mode (terminal/gui): ").strip().lower()
if mode == "terminal":
    from terminal_ui import main
    main()
elif mode == "gui":
    import tkinter as tk
    from gui_app import BudgetApp
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
else:
    print("Invalid mode.")