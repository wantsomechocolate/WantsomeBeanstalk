# coding: utf8
db.define_table('electric',
                Field('TotalElectricEnergyPurchasedByOrganization','float'),
                Field('TotalElectricEnergyPurchasedByOrganizationUnits','string'),
                Field('TotalElectricEnergyPurchasedByDirectlyMeteredTenants','float'),
                Field('TotalElectricEnergyPurchasedByDirectlyMeteredTenantsUnits','string'),
                Field('TotalElectricEnergyPurchasedBySubMeteredTenants','float'),
                Field('TotalElectricEnergyPurchasedBySubMeteredTenantsUnits','string')
                )
