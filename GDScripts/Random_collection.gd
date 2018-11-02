
Have button hide an menu.
func _on_CancelButton_pressed():

	if popup_pass_turn_menu.is_visible():
		#print("Cancel pass turn")
		popup_pass_turn_menu.hide()


Short timeout:


get_tree().paused = true
yield(get_tree().create_timer(0.075), 'timeout')
get_tree().paused = false


Wait for function:
function 1 is waiting for function 2:
function 1:
yield(node_instance, signal_name)

function 2:
node_instance.emit_signal(signal_name)






count_numbers


func do_thing():
    a_node.call_deferred("execute")
    yield(a_node,"executed")




# In the a_node script:
signal executed(val)
func execute():
    OS.delay_msecs(100)
    emit_signal("executed",123)