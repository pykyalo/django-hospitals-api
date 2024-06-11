from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class Hospital(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    lo = models.FloatField(_("Longitude"))
    la = models.FloatField(_("Latitude"))
    fi = models.IntegerField(_("Field ID"))
    beds = models.IntegerField(_("Bed Numbers"), default=1)
    province_name = models.CharField(_("Province Name"), max_length=100)
    province_code = models.CharField(_("Province Code"), max_length=1)
    geom = models.PointField(srid=4326)

    class Meta:
        verbose_name = _("Hospitals")
        verbose_name_plural = _("Hospitals")

    def __str__(self):
        return self.name
