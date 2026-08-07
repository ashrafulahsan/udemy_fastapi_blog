def total_price(price1: float, price2: float) -> float:   
    return price1 + price2

sum = total_price('10.5', '20.3')

print(f"The total price is: {sum}")

# from typing import List, Tuple, Dict

# price: List[float] = [10.5, 20.3, 30.0]
# price: Tuple[float, float, float] = (10.5, 20.3, 30.0)
# price: Dict[str, float] = {
#     "item1": 10.5, 
#     "item2": 20.3, 
#     "item3": 30.0
#     }

# from typing import Union, List, Optional, Any, Callable

# price: List[Union[float, int]] = [10.5, 20, 30, 40.0]


# def inr_to_usd(value: float) -> Union[float, None]:
#     return value / 82.0

# inr_to_usd('2323.0')