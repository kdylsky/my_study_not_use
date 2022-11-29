class NumberService:
    def set_text(self, number_obj):
        if number_obj.number < 0:
            number_obj.text = "N"
        elif number_obj.number == 0:
            number_obj.text = "Z"
        else:
            number_obj.text = "P"
        number_obj.save()
        