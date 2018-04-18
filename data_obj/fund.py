class Fund(object):
    def __init__(self, fund_id, fund_code, fund_name, fund_invest_style, fund_date, fund_unit, fund_accumulated, fund_comment, fund_five, fund_ten, fund_twenty, fund_forty, fund_sixty, fund_enhance_normalization, fund_enhance):
        super(Fund, self).__init__()
        self.id = fund_id
        self.code = fund_code
        self.name = fund_name
        self.invest_style = fund_invest_style
        self.date = fund_date
        self.unit = fund_unit
        self.accumulated = fund_accumulated
        self.comment = fund_comment
        self.five = fund_five
        self.ten = fund_ten
        self.twenty = fund_twenty
        self.forty = fund_forty
        self.sixty = fund_sixty
        self.enhance_normalization = fund_enhance_normalization
        self.enhance = fund_enhance



