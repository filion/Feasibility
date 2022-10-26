class BaseEntity:
    def __init__(self, entity_name, entity_type):
        self.name = entity_name
        self.type = entity_type
        """
        Market Schedule to be read after initialization
        """
        # TODO: decide when to fill those attributes
        self.market_schedule = None
        self.max_afrr = None
        self.min_afrr = None
        self.max_mfrr = None
        self.min_mfrr = None
        self.max_fcr = None
        self.min_fcr = None
        self.min_up = None
        self.min_down = None
        # TODO: decide if those will be tranfered to more specific classes (CCGT)
        self.technical_minimum = None
        self.maximum_availability = None

    def set_market_schedule(self, market_schedule):
        self.market_schedule = market_schedule


class ThermalEntity(BaseEntity):
    def __init__(self, entity_name, entity_type):
        super().__init__(entity_name, entity_type)

        # TODO: What to fill here?


class ThermalCCGT(ThermalEntity):
    def __init__(self, entity_name, entity_type):
        super().__init__(entity_name, entity_type)
        self.ccgt = dict()


class ThermalBiFuel(ThermalEntity):
    def __init__(self, entity_name, entity_type):
        super().__init__(entity_name, entity_type)
        self.fuels = dict()


class HydroEntity(BaseEntity):
    def __init__(self, entity_name, entity_type):
        super.__init__(entity_name, entity_type)
        self.mandatory_hydro_schedule = None
        self.generators = dict()

    def set_mandatory_hydro_schedule(self, mandatory_schedule):
        self.mandatory_hydro_schedule = mandatory_schedule
