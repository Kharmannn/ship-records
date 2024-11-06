class LocatorConfig:
    FLAG = {
        "xpath": "//div[@class='col-lg-4 col-md-6 m-b-sm' and .//small[contains(text(), 'Flag')]]",
        "name": "Flag"
    } 
    VESSEL_NAME = {
        "xpath": "(.//div[@class='ibox-title product-name producTitle'])[{0}]",
        "name": "Vessel Name"
    }
    IMO_NUMBER = {
        "xpath": "(.//div[@class='ibox-content min-height-125px']//div[contains(text(), 'IMO Number')])[{0}]",
        "name": "IMO Number"
    }
    FLAG = {
        "xpath": "//div[@class='col-lg-4 col-md-6 m-b-sm' and .//small[contains(text(), 'Flag')]]",
        "name": "Flag"
    }
    LAUNCH_DATE = {
        "xpath": ".//li[.//*[contains(text(), 'Launch Date')]]//small",
        "name": "Launch Date"
    }
    DESIGN_DWT = {
        "xpath": ".//li[.//*[contains(text(), 'Design Deadweight')]]//small",
        "name": "Design Deadweight"
    }
    GROSS_TONNAGE = {
        "xpath": "(.//div[@class='label-value' and .//small[contains(text(), 'ITC')] and .//h5[contains(text(), 'Gross Tonnage')]]//small)[2]",
        "name": "Gross Tonnage"
    }
    CB = {
        "xpath": ".//li[.//*[contains(text(), 'Block Coefficient Class (Cb)')]]//small",
        "name": "Block Coefficient Class (Cb)"
    }
    DISPLACEMENT = {
        "xpath": "(.//li[.//*[contains(text(), 'Displacement (tonnes)')]]//small)[1]",
        "name": "Displacement (tonnes)"
    }
    DESIGN_SPEED = {
        "xpath": ".//li[.//*[contains(text(), 'Design Speed Ahead')]]//small",
        "name": "Design Speed Ahead"
    }
    LOA = {
        "xpath": ".//li[.//*[contains(text(), 'LOA')]]//small",
        "name": "Length Overall (LOA)"
    }
    FREEBOARD = {
        "xpath": "(.//li[.//*[contains(text(), 'Calculated Freeboard (mm)')]]//small)[1]",
        "name": "Calculated Freeboard (mm)"
    }
    BREADTH = {
        "xpath": "(.//li[.//*[contains(text(), 'Breadth Overall')]]//small)[1]",
        "name": "Breadth Overall"
    }
    HEIGHT = {
        "xpath": "(.//li[.//*[contains(text(), 'Depth Overall')]]//small)[1]",
        "name": "Depth Overall"
    }
    LPP = {
        "xpath": "(.//li[.//*[contains(text(), 'Length Between Perpendicular')]]//small)[1]",
        "name": "Length Between Perpendicular (LPP)"
    }
    DRAFT_DESIGN = {
        "xpath": "(.//li[.//*[contains(text(), 'Design Draft')]]//small)[1]",
        "name": "Design Draft"
    }
    DRAFT_MOLDED = {
        "xpath": "(.//li[.//*[contains(text(), 'Draft Molded')]]//small)[1]",
        "name": "Draft Molded"
    }
    DRAFT_SCANTLING = {
        "xpath": "(.//li[.//*[contains(text(), 'Draft Scantling')]]//small)[1]",
        "name": "Draft Scantling"
    }
    NUMBER_GENERATOR = {
        "xpath": ".//div[@class='row' and contains(text(), 'Generator')]",
        "name": "Generator Number"
    }
    AE_RATED_POWER = {
        "xpath": "(.//div[@class='col-lg-4' and .//strong[contains(text(), 'Rated Power')]])[1]",
        "name": "Auxiliary Engine Rated Power"
    }
    AE_MANUFACTURER = {
        "xpath": "(.//div[@class='TreeListItem undefined' and .//*[contains(text(), 'Generator')]]//div[@class='col-lg-4' and contains(., 'Manufacturer Name')])[1]",
        "name": "Auxiliary Engine Manufacturer"
    }
    AE_MODEL_NUMBER = {
        "xpath": "(.//div[@class='TreeListItem undefined' and .//*[contains(text(), 'Generator')]]//div[@class='col-lg-4' and contains(., 'Model Number')])[1]",
        "name": "Auxiliary Engine Model Number"
    }
    ME_MANUFACTURER = {
        "xpath": "(.//div[contains(text(), 'Main Engine') or contains(text(), 'Main Diesel Engine') or contains(text(), 'MAIN ENGINE')]//following::div[contains(., 'Manufacturer Name')])[3]",
        "name": "Main Engine Manufacturer"
    }
    ME_MODEL_NUMBER = {
        "xpath": "(.//div[contains(text(), 'Main Engine') or contains(text(), 'Main Diesel Engine') or contains(text(), 'MAIN ENGINE')]//following::div[contains(., 'Model Number')])[3]",
        "name": "Main Engine Model Number"
    }
    ME_RATED_POWER = {
        "xpath": "(.//div[contains(text(), 'Main Engine') or contains(text(), 'Main Diesel Engine') or contains(text(), 'MAIN ENGINE')]//following::div[contains(., 'Maximum Continuous Rating')])[3]",
        "name": "Main Engine Rated Power"
    }
    COL_VESSEL_DETAIL = {
        "xpath": ".//div[@class='VesselDetailsCard abs-detail-card']",
        "name": "Vessel Details Column"
    }
    COL_VESSEL_MACHINERY = {
        "xpath": ".//div[@class='row' and .//*[contains(text(), 'Vessel Assets')]]",
        "name": "Vessel Machinery Column"
    }
    BTN_DROPDOWN_SHIP_TYPE = {
        "xpath": ".//input[@value='Choose Vessel Type']",
        "name": "Button Dropdown Ship Type"
    }
    BTN_SEARCH = {
        "xpath": "//button[text()=' Search']",
        "name": "Button Search"
    }
    BTN_ASSETS = {
        "xpath": ".//li[@class='Ripple-parent' and .//*[contains(text(), 'Assets')]]",
        "name": "Button Assets"
    }
    BTN_OWNER = {
        "xpath": ".//li[@class='Ripple-parent' and .//*[contains(text(), 'Owner')]]",
        "name": "Button Assets"
    }
    BTN_VESSEL_NAME = {
        "xpath": "(.//div[@class='ABSRecordCard'])[{0}]",
        "name": "Button Vessel Name"
    }
    OPT_SHIP_TYPE = {
        "xpath": ".//li/span[text()='{0}']",
        "name": "Option Dropdown Ship Type Bulk Carrier"
    }