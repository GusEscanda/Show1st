/* 
Swaps the style.display value of the two elements received.
- Tipycaly one of them has the display='none' and the other some other value, 
  so the effect is that one get hidden and the other shows up. 
- Also tipycaly you may call the function twice, one to swap the elements and 
  the other to swap the link that triggers the swapping, so you can "change"
  it's text or image
*/

const swapDisplay = (_elementIdA, _elementIdB) => {
    const elementA = document.getElementById(_elementIdA)
    const elementB = document.getElementById(_elementIdB)
    const displayA = elementA.style.display
    const displayB = elementB.style.display
    elementA.style.display = displayB
    elementB.style.display = displayA
}


const popUp = (_url) => {
    popUpWindow = window.open( _url,
                               'popUpWindow',
                               'height=10, width=10, left=10, top=10, resizable=no, scrollbars=no, toolbar=no, menubar=no, location=no, directories=no, status=no'
               );
    // popUpWindow.close()
}

