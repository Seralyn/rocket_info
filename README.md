# rocket_info
An application to learn about and compare various rocket models.

This is the first run of code that will form the foundation of the eventual application.

A note on the method of calculation for sorting and comparisons: 
-If there is more than one variant of a rocket, the strongest configuration will be used for sorting and graphing.
-To calculate the thrust for comparison, I have added the thrust of the booster to the thrust of the first stage, forming a variabled named "initial_thrust" and that is used except when a rocket does not engage its first stage engines until after the boosters have completed their burn. In that case, I have used whichever thrust rating is higher.
-To calculate the "burn time" I have added the burn times of each stage together, except the boosters (if present), assuming their burn time is less than the first stage burn time. If their burn time is longer than the first stage, I have used that.
-To calculate specific impulse, I have added the boosters and first stage together and taken the average and used that as the metric by which to measure and compare. For vacuum metrics, I have used only the final stage as it is most likely the stage to be used in complete vacuum, rather than a middle stage which may burn partially at thin atmosphere and partially in vacuum.

A note on the Cost Per Launch category:
I have converted all costs per launch to the value in 2019 USD for the sake of clarity and consistency.
