# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities
from . import outputs

__all__ = [
    'GetCartProductOptionsPlanPriceResult',
    'GetCartProductOptionsPlanPricePriceResult',
    'GetCartProductOptionsPlanSelectedPriceResult',
    'GetCartProductOptionsPlanSelectedPricePriceResult',
    'GetCartProductOptionsResultResult',
    'GetCartProductOptionsResultPriceResult',
    'GetCartProductOptionsResultPricePriceResult',
    'GetCartProductPlanPriceResult',
    'GetCartProductPlanPricePriceResult',
    'GetCartProductPlanSelectedPriceResult',
    'GetCartProductPlanSelectedPricePriceResult',
    'GetCartProductResultResult',
    'GetCartProductResultPriceResult',
    'GetCartProductResultPricePriceResult',
]

@pulumi.output_type
class GetCartProductOptionsPlanPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductOptionsPlanPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductOptionsPlanPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductOptionsPlanPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductOptionsPlanPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetCartProductOptionsPlanSelectedPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductOptionsPlanSelectedPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductOptionsPlanSelectedPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductOptionsPlanSelectedPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductOptionsPlanSelectedPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetCartProductOptionsResultResult(dict):
    def __init__(__self__, *,
                 exclusive: bool,
                 family: str,
                 mandatory: bool,
                 plan_code: str,
                 prices: Sequence['outputs.GetCartProductOptionsResultPriceResult'],
                 product_name: str,
                 product_type: str):
        """
        :param bool exclusive: Define if options of this family are exclusive with each other
        :param str family: Option family
        :param bool mandatory: Define if an option of this family is mandatory
        :param str plan_code: Product offer identifier
        :param Sequence['GetCartProductOptionsResultPriceArgs'] prices: Prices of the product offer
        :param str product_name: Name of the product
        :param str product_type: Product type
        """
        pulumi.set(__self__, "exclusive", exclusive)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "mandatory", mandatory)
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "product_name", product_name)
        pulumi.set(__self__, "product_type", product_type)

    @property
    @pulumi.getter
    def exclusive(self) -> bool:
        """
        Define if options of this family are exclusive with each other
        """
        return pulumi.get(self, "exclusive")

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        Option family
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def mandatory(self) -> bool:
        """
        Define if an option of this family is mandatory
        """
        return pulumi.get(self, "mandatory")

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> str:
        """
        Product offer identifier
        """
        return pulumi.get(self, "plan_code")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductOptionsResultPriceResult']:
        """
        Prices of the product offer
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> str:
        """
        Name of the product
        """
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> str:
        """
        Product type
        """
        return pulumi.get(self, "product_type")


@pulumi.output_type
class GetCartProductOptionsResultPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductOptionsResultPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductOptionsResultPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductOptionsResultPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductOptionsResultPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetCartProductPlanPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductPlanPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductPlanPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductPlanPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductPlanPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetCartProductPlanSelectedPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductPlanSelectedPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductPlanSelectedPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductPlanSelectedPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductPlanSelectedPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class GetCartProductResultResult(dict):
    def __init__(__self__, *,
                 plan_code: str,
                 prices: Sequence['outputs.GetCartProductResultPriceResult'],
                 product_name: str,
                 product_type: str):
        """
        :param str plan_code: Product offer identifier
        :param Sequence['GetCartProductResultPriceArgs'] prices: Prices of the product offer
        :param str product_name: Name of the product
        :param str product_type: Product type
        """
        pulumi.set(__self__, "plan_code", plan_code)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "product_name", product_name)
        pulumi.set(__self__, "product_type", product_type)

    @property
    @pulumi.getter(name="planCode")
    def plan_code(self) -> str:
        """
        Product offer identifier
        """
        return pulumi.get(self, "plan_code")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductResultPriceResult']:
        """
        Prices of the product offer
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> str:
        """
        Name of the product
        """
        return pulumi.get(self, "product_name")

    @property
    @pulumi.getter(name="productType")
    def product_type(self) -> str:
        """
        Product type
        """
        return pulumi.get(self, "product_type")


@pulumi.output_type
class GetCartProductResultPriceResult(dict):
    def __init__(__self__, *,
                 capacities: Sequence[Any],
                 description: str,
                 duration: str,
                 interval: int,
                 maximum_quantity: int,
                 maximum_repeat: int,
                 minimum_quantity: int,
                 minimum_repeat: int,
                 price_in_ucents: int,
                 prices: Sequence['outputs.GetCartProductResultPricePriceResult'],
                 pricing_mode: str,
                 pricing_type: str):
        """
        :param Sequence[Any] capacities: Capacities of the pricing (type of pricing)
        :param str description: Description of the pricing
        :param str duration: Duration for ordering the product
        :param int interval: Interval of renewal
        :param int maximum_quantity: Maximum quantity that can be ordered
        :param int maximum_repeat: Maximum repeat for renewal
        :param int minimum_quantity: Minimum quantity that can be ordered
        :param int minimum_repeat: Minimum repeat for renewal
        :param int price_in_ucents: Price of the product in micro-centims
        :param Sequence['GetCartProductResultPricePriceArgs'] prices: Price of the product (Price with its currency and textual representation)
        :param str pricing_mode: Pricing model identifier
        :param str pricing_type: Pricing type
        """
        pulumi.set(__self__, "capacities", capacities)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "maximum_quantity", maximum_quantity)
        pulumi.set(__self__, "maximum_repeat", maximum_repeat)
        pulumi.set(__self__, "minimum_quantity", minimum_quantity)
        pulumi.set(__self__, "minimum_repeat", minimum_repeat)
        pulumi.set(__self__, "price_in_ucents", price_in_ucents)
        pulumi.set(__self__, "prices", prices)
        pulumi.set(__self__, "pricing_mode", pricing_mode)
        pulumi.set(__self__, "pricing_type", pricing_type)

    @property
    @pulumi.getter
    def capacities(self) -> Sequence[Any]:
        """
        Capacities of the pricing (type of pricing)
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Description of the pricing
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        Duration for ordering the product
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def interval(self) -> int:
        """
        Interval of renewal
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter(name="maximumQuantity")
    def maximum_quantity(self) -> int:
        """
        Maximum quantity that can be ordered
        """
        return pulumi.get(self, "maximum_quantity")

    @property
    @pulumi.getter(name="maximumRepeat")
    def maximum_repeat(self) -> int:
        """
        Maximum repeat for renewal
        """
        return pulumi.get(self, "maximum_repeat")

    @property
    @pulumi.getter(name="minimumQuantity")
    def minimum_quantity(self) -> int:
        """
        Minimum quantity that can be ordered
        """
        return pulumi.get(self, "minimum_quantity")

    @property
    @pulumi.getter(name="minimumRepeat")
    def minimum_repeat(self) -> int:
        """
        Minimum repeat for renewal
        """
        return pulumi.get(self, "minimum_repeat")

    @property
    @pulumi.getter(name="priceInUcents")
    def price_in_ucents(self) -> int:
        """
        Price of the product in micro-centims
        """
        return pulumi.get(self, "price_in_ucents")

    @property
    @pulumi.getter
    def prices(self) -> Sequence['outputs.GetCartProductResultPricePriceResult']:
        """
        Price of the product (Price with its currency and textual representation)
        """
        return pulumi.get(self, "prices")

    @property
    @pulumi.getter(name="pricingMode")
    def pricing_mode(self) -> str:
        """
        Pricing model identifier
        """
        return pulumi.get(self, "pricing_mode")

    @property
    @pulumi.getter(name="pricingType")
    def pricing_type(self) -> str:
        """
        Pricing type
        """
        return pulumi.get(self, "pricing_type")


@pulumi.output_type
class GetCartProductResultPricePriceResult(dict):
    def __init__(__self__, *,
                 currency_code: str,
                 text: str,
                 value: float):
        """
        :param str currency_code: Currency code
        :param str text: Textual representation
        :param float value: The effective price
        """
        pulumi.set(__self__, "currency_code", currency_code)
        pulumi.set(__self__, "text", text)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="currencyCode")
    def currency_code(self) -> str:
        """
        Currency code
        """
        return pulumi.get(self, "currency_code")

    @property
    @pulumi.getter
    def text(self) -> str:
        """
        Textual representation
        """
        return pulumi.get(self, "text")

    @property
    @pulumi.getter
    def value(self) -> float:
        """
        The effective price
        """
        return pulumi.get(self, "value")


