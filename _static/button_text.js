    //Select button by id
    const MyButton = document.getElementById('MyButton');
    //Add on click listener for button
    MyButton.addEventListener('click', function() {
        //Select (h1) heading by id, and then change it's value to (bananas)
        document.getElementById('MyHeading').innerText = "bananas"
    })