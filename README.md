# Installation instructions (Windows):

1. Install VScode (or your IDE of choice)
2. Install WSL `wsl --install`
3. Install Python `sudo apt-get install python3`
4. Install Pip `sudo apt-get install python3-pip`
5. Install Pytest `pip install pytest`
6. Install Taskwarrior `sudo apt install taskwarrior`
7. Install Requests `pip install pytest requests`


# Part 1: TaskWarrior automation scenarios
1. User can create and display list - Automated
2. User can modify existing list - Automated
3. User can modify due dates - Automated
4. User can use filter to list exact task - Automated  
5. User can use Show functionality - TBD

# Part 2: Fakestore API Tests
1. Verify data in a single user's cart - Automated
2. Verify data is pulled from all carts - Automated
3. Verify carts are pulled in a limited selection - Not Automated
4. Add new product to user's cart - Automated - as per seed data
5. Update new product in user's cart - Automated - as per seed data
6. Delete a cart - Automated - as per seed data
7. User can acquire carts within a date range - Not Automated
8. User can sort results - Not automated

# Future Improvements
## CLI with TaskWarrior
1. Debugging filters test. Unsure why on runtime with Pytest the test runner stalls during global cleanup commands (delete/purge).
2. Boundry limit tests; pushing multiple tasks (tens-hundreds) and expecting data
3. Adding Show functionality to taskwarrior auto scripts

## API with FakeStore
1. Cart limited selection queries; deprioritized due to being lower-impact than update/delete requests
2. Cart filters via date range; deprioritized same as above
3. Sort Results test; deprioritized as above
