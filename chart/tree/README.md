# favorite-tree

![Version: 1.0.0-dev](https://img.shields.io/badge/Version-1.0.0--dev-informational?style=flat-square)

Tree Api that returns my favorite tree in json.

**Homepage:** <https://techtative.io>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| moabu | mo@techtative.io |  |

## Source Code

* <https://github.com/moabu/tree/api>

## Requirements

Kubernetes: `>=v1.21.0-0`

| Repository | Name | Version |
|------------|------|---------|
|  | tree-api | 1.0.0-dev |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| tree-api | object | `{"additionalAnnotations":{},"additionalLabels":{},"configmap":{"flaskApp":"main.core:app","flaskEnv":"development","guncornLogLevel":"debug","sqlalchemyDatabaseSecretName":"sql-secret-uri","sqlalchemyDatabaseUriFilepath":"/sql_secrets/uri"},"dnsConfig":{},"dnsPolicy":"","hack":{"enabled":false,"favoriteTree":"Olive Tree"},"hpa":{"behavior":{},"enabled":true,"maxReplicas":10,"metrics":[],"minReplicas":1,"targetCPUUtilizationPercentage":50},"image":{"pullPolicy":"IfNotPresent","pullSecrets":[],"repository":"abudayyehwork/tree-api","tag":"1.0.0_dev"},"ingress":{"alb":{"enabled":false},"hosts":["my.ecosia.org"],"istio":{"enabled":false},"nginx":{"enabled":true,"ingresClass":"nginx"},"path":"/","tls":[{"hosts":["my.ecosia.org"],"secretName":"tls-certificate"}],"treeApiAdditionalAnnotations":{},"treeApiLabels":{}},"livenessProbe":{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":5},"readinessProbe":{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":25,"periodSeconds":25,"timeoutSeconds":5},"replicas":1,"resources":{"limits":{"cpu":"500m","memory":"500Mi"},"requests":{"cpu":"500m","memory":"500Mi"}},"service":{"name":"tree-api","port":5000,"sessionAffinity":"None","sessionAffinityConfig":{"clientIP":{"timeoutSeconds":10800}}},"testEnviroment":true,"usrEnvs":{"normal":{},"secret":{}},"volumeMounts":[],"volumes":[]}` | Tree Api that returns my favorite tree in json. |
| tree-api.additionalAnnotations | object | `{}` | Additional annotations that will be added across all resources  in the format of {cert-manager.io/issuer: "letsencrypt-prod"}. key app is taken |
| tree-api.additionalLabels | object | `{}` | Additional labels that will be added across all resources definitions in the format of {mylabel: "myapp"} |
| tree-api.configmap.flaskEnv | string | `"development"` | Sets the flask env. development, production, testing, staging |
| tree-api.configmap.guncornLogLevel | string | `"debug"` | Sets the guncorn log level info, error, debug, trace |
| tree-api.configmap.sqlalchemyDatabaseSecretName | string | `"sql-secret-uri"` | secret holding the sql uri |
| tree-api.configmap.sqlalchemyDatabaseUriFilepath | string | `"/sql_secrets/uri"` | file path of the sql uri string containing the connection params |
| tree-api.dnsConfig | object | `{}` | Add custom dns config |
| tree-api.dnsPolicy | string | `""` | Add custom dns policy |
| tree-api.hack | object | `{"enabled":false,"favoriteTree":"Olive Tree"}` | ditches the API and disables the deployment and instead parses the ingress to display the favorite tree. works only with nginx ingress |
| tree-api.hack.enabled | bool | `false` | boolean flag that disables the deployment and instead parses the ingress to display the favorite tree. |
| tree-api.hack.favoriteTree | string | `"Olive Tree"` | Your favorite tree |
| tree-api.hpa | object | `{"behavior":{},"enabled":true,"maxReplicas":10,"metrics":[],"minReplicas":1,"targetCPUUtilizationPercentage":50}` | Configure the HorizontalPodAutoscaler |
| tree-api.hpa.behavior | object | `{}` | Scaling Policies |
| tree-api.hpa.metrics | list | `[]` | metrics if targetCPUUtilizationPercentage is not set |
| tree-api.image.pullPolicy | string | `"IfNotPresent"` | Image pullPolicy to use for deploying. |
| tree-api.image.pullSecrets | list | `[]` | Image Pull Secrets |
| tree-api.image.repository | string | `"abudayyehwork/tree-api"` | Image  to use for deploying. |
| tree-api.image.tag | string | `"1.0.0_dev"` | Image  tag to use for deploying. |
| tree-api.ingress.alb.enabled | bool | `false` | Activates ALB ingress |
| tree-api.ingress.istio | object | `{"enabled":false}` | enable istio sidecars |
| tree-api.ingress.istio.enabled | bool | `false` | Boolean flag that enables using istio side cars with Janssen services. |
| tree-api.ingress.nginx.enabled | bool | `true` | Boolean flag that enables using ingress definition that integrates with Nginx. |
| tree-api.ingress.tls | list | `[{"hosts":["my.ecosia.org"],"secretName":"tls-certificate"}]` | Secrets holding HTTPS CA cert and key. |
| tree-api.ingress.treeApiAdditionalAnnotations | object | `{}` | tree api ingress resource additional annotations. |
| tree-api.ingress.treeApiLabels | object | `{}` | tree api ingress resource labels. key app is taken |
| tree-api.livenessProbe | object | `{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":5}` | Configure the liveness healthcheck for the tree-api if needed. |
| tree-api.livenessProbe.httpGet | object | `{"path":"/tree","port":5000}` | Executes the python3 healthcheck. |
| tree-api.livenessProbe.httpGet.path | string | `"/tree"` | http readiness probe endpoint |
| tree-api.readinessProbe | object | `{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":25,"periodSeconds":25,"timeoutSeconds":5}` | Configure the readiness healthcheck for the tree-api if needed. |
| tree-api.readinessProbe.httpGet.path | string | `"/tree"` | http readiness probe endpoint |
| tree-api.replicas | int | `1` | Service replica number. |
| tree-api.resources | object | `{"limits":{"cpu":"500m","memory":"500Mi"},"requests":{"cpu":"500m","memory":"500Mi"}}` | Resource specs. |
| tree-api.resources.limits.cpu | string | `"500m"` | CPU limit. |
| tree-api.resources.limits.memory | string | `"500Mi"` | Memory limit. |
| tree-api.resources.requests.cpu | string | `"500m"` | CPU request. |
| tree-api.resources.requests.memory | string | `"500Mi"` | Memory request. |
| tree-api.service.name | string | `"tree-api"` | The name of the tree-api port within the tree-api service. Please keep it as default. |
| tree-api.service.port | int | `5000` | Port of the tree-api service. Please keep it as default. |
| tree-api.service.sessionAffinity | string | `"None"` | Default set to None If you want to make sure that connections from a particular client are passed to the same Pod each time, you can select the session affinity based on the client's IP addresses by setting this to ClientIP |
| tree-api.service.sessionAffinityConfig | object | `{"clientIP":{"timeoutSeconds":10800}}` | the maximum session sticky time if sessionAffinity is ClientIP |
| tree-api.testEnviroment | bool | `true` | Boolean flag if enabled will strip resources requests and limits from deployments. |
| tree-api.usrEnvs | object | `{"normal":{},"secret":{}}` | Add custom normal and secret envs to the service |
| tree-api.usrEnvs.normal | object | `{}` | Add custom normal envs to the service variable1: value1 |
| tree-api.usrEnvs.secret | object | `{}` | Add custom secret envs to the service variable1: value1 |
| tree-api.volumeMounts | list | `[]` | Configure any additional volumesMounts that need to be attached to the containers |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.7.0](https://github.com/norwoodj/helm-docs/releases/v1.7.0)
