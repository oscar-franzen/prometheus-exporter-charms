#!/usr/bin/python3
"""PrometheusSlurmExporterProvides."""
from ops.framework import Object


class PrometheusSlurmExporterProvides(Object):
    """PrometheusSlurmExporterProvides."""

    def __init__(self, charm, relation):
        """Set the initial values."""
        super().__init__(charm, relation)
        self._charm = charm
        self._relation_name = relation

        self.framework.observe(
            self._charm.on[self._relation_name].relation_created,
            self._on_relation_created
        )

    def _on_relation_created(self, event):
        if self._charm.is_prometheus_slurm_exporter_installed():
            event.relation.data[self.model.unit]['hostname'] = \
                event.relation.data[self.model.unit]['ingress-address']
            event.relation.data[self.model.unit]['port'] = "8080"
            event.relation.data[self.model.unit]['metrics_path'] = "/metrics"
        else:
            event.defer()
