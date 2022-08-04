# tree-api

![Version: 1.0.0-dev](https://img.shields.io/badge/Version-1.0.0--dev-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0-dev](https://img.shields.io/badge/AppVersion-1.0.0--dev-informational?style=flat-square)

Tree Api that returns my favorite tree in json.

**Homepage:** <https://techtative.io>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| Mohammad Abudayyeh | mo@techtative.io | https://github.com/moabu |

## Source Code

* <https://github.com/moabu/tree/api>

## Requirements

Kubernetes: `>=v1.21.0-0`

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| additionalAnnotations | object | `{}` | Additional annotations that will be added across all resources  in the format of {cert-manager.io/issuer: "letsencrypt-prod"}. key app is taken |
| additionalLabels | object | `{}` | Additional labels that will be added across all resources definitions in the format of {mylabel: "myapp"} |
| configmap.flaskApp | string | `"main.core:app"` |  |
| configmap.flaskEnv | string | `"development"` | Sets the flask env. development, production, testing, staging |
| configmap.guncornLogLevel | string | `"debug"` | Sets the guncorn log level info, error, debug, trace |
| dnsConfig | object | `{}` | Add custom dns config |
| dnsPolicy | string | `""` | Add custom dns policy |
| hpa | object | `{"behavior":{},"enabled":true,"maxReplicas":10,"metrics":[],"minReplicas":1,"targetCPUUtilizationPercentage":50}` | Configure the HorizontalPodAutoscaler |
| hpa.behavior | object | `{}` | Scaling Policies |
| hpa.metrics | list | `[]` | metrics if targetCPUUtilizationPercentage is not set |
| image.pullPolicy | string | `"IfNotPresent"` | Image pullPolicy to use for deploying. |
| image.pullSecrets | list | `[]` | Image Pull Secrets |
| image.repository | string | `"abudayyehwork/tree-api"` | Image  to use for deploying. |
| image.tag | string | `"1.0.0_dev"` | Image  tag to use for deploying. |
| ingress.alb.enabled | bool | `false` | Activates ALB ingress |
| ingress.hosts[0] | string | `"my.ecosia.org"` |  |
| ingress.istio | object | `{"enabled":false}` | enable istio sidecars |
| ingress.istio.enabled | bool | `false` | Boolean flag that enables using istio side cars with Janssen services. |
| ingress.nginx.enabled | bool | `true` | Boolean flag that enables using ingress definition that integrates with Nginx. |
| ingress.nginx.ingresClass | string | `"nginx"` |  |
| ingress.path | string | `"/"` |  |
| ingress.tls | list | `[{"hosts":["my.ecosia.org"],"secretName":"tls-certificate"}]` | Secrets holding HTTPS CA cert and key. |
| ingress.treeApiAdditionalAnnotations | object | `{}` | tree api ingress resource additional annotations. |
| ingress.treeApiLabels | object | `{}` | tree api ingress resource labels. key app is taken |
| livenessProbe | object | `{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":5}` | Configure the liveness healthcheck for the tree-api if needed. |
| livenessProbe.httpGet | object | `{"path":"/tree","port":5000}` | Executes the python3 healthcheck. |
| livenessProbe.httpGet.path | string | `"/tree"` | http readiness probe endpoint |
| readinessProbe | object | `{"httpGet":{"path":"/tree","port":5000},"initialDelaySeconds":25,"periodSeconds":25,"timeoutSeconds":5}` | Configure the readiness healthcheck for the tree-api if needed. |
| readinessProbe.httpGet.path | string | `"/tree"` | http readiness probe endpoint |
| replicas | int | `1` | Service replica number. |
| resources | object | `{"limits":{"cpu":"500m","memory":"500Mi"},"requests":{"cpu":"500m","memory":"500Mi"}}` | Resource specs. |
| resources.limits.cpu | string | `"500m"` | CPU limit. |
| resources.limits.memory | string | `"500Mi"` | Memory limit. |
| resources.requests.cpu | string | `"500m"` | CPU request. |
| resources.requests.memory | string | `"500Mi"` | Memory request. |
| service.name | string | `"tree-api"` | The name of the tree-api port within the tree-api service. Please keep it as default. |
| service.port | int | `5000` | Port of the tree-api service. Please keep it as default. |
| service.sessionAffinity | string | `"None"` | Default set to None If you want to make sure that connections from a particular client are passed to the same Pod each time, you can select the session affinity based on the client's IP addresses by setting this to ClientIP |
| service.sessionAffinityConfig | object | `{"clientIP":{"timeoutSeconds":10800}}` | the maximum session sticky time if sessionAffinity is ClientIP |
| testEnviroment | bool | `true` | Boolean flag if enabled will strip resources requests and limits from deployments. |
| usrEnvs | object | `{"normal":{},"secret":{}}` | Add custom normal and secret envs to the service |
| usrEnvs.normal | object | `{}` | Add custom normal envs to the service variable1: value1 |
| usrEnvs.secret | object | `{}` | Add custom secret envs to the service variable1: value1 |
| volumeMounts | list | `[]` | Configure any additional volumesMounts that need to be attached to the containers |
| volumes | list | `[]` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.7.0](https://github.com/norwoodj/helm-docs/releases/v1.7.0)
