from datetime import date, timedelta

import pytest
from ecommerce.promotion.models import Promotion
from ecommerce.promotion.tasks import promotion_management, promotion_prices


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (date.today(), date.today() + timedelta(5), True),
        (date.today() - timedelta(10), date.today() - timedelta(5), False),
        (date.today() + timedelta(5), date.today() + timedelta(10), False),
    ],
)
def test_promotion_management(start, end, expected, celery_app, celery_worker, promotion_multi_variant):

    promotion_multi_variant.promo_start = start
    promotion_multi_variant.promo_end = end
    promotion_multi_variant.save(update_fields=["promo_start", "promo_end"])
    promotion_management()
    promotion = Promotion.objects.all().first()
    assert promotion.is_active == expected


@pytest.mark.parametrize(
    "reduction, result",
    [
        (10, 90),
        (50, 50),
    ],
)
def test_promotion_price_reduction(reduction, result, celery_app, celery_worker, promotion_multi_variant):
    promotion_prices(reduction, promotion_multi_variant.id)
    new_price = Promotion.products_on_promotion.through.objects.get(promotion_id=promotion_multi_variant.id)
    assert new_price.promo_price == result
