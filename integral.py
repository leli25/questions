def get_integral_from_data(acceleration_data, times):
    # 1. We will need to keep track of the total accumulated speed
    accumulated_speed = 0.0
    
    # 2. The next lines should look familiar from the derivative code
    last_time = times[0]
    speeds = []
    
    # 3. Once again, we lose some data because we have to start
    #    at i=1 instead of i=0.
    for i in range(1, len(times)):
        
        # 4. Get the numbers for this index i
        acceleration = acceleration_data[i]
	# demo is using acceleration_data[i], but I think it should be acceleration_data[i-1] ???
        time = times[i]
        
        # 5. Calculate delta t
        delta_t = time - last_time
        
        # 6. This is an important step! This is where we approximate
        #    the area under the curve using a rectangle w/ width of
        #    delta_t.
        delta_v = acceleration * delta_t
        
        # 7. The actual speed now is whatever the speed was before
        #    plus the new change in speed.
        accumulated_speed += delta_v
        
        # 8. append to speeds and update last_time
        speeds.append(accumulated_speed)
        last_time = time
    return speeds
