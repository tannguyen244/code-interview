1. Write a Helm chart to quickly test and validate multiple ingress paths. the content returned for each host should equal the hostname (see example use case below).

   `values.yaml` expected format
   
   ```yaml
   domain: gw.skymavis.xyz

   ingressAnnotations: {}
     # # for example 
     # kubernetes.io/ingress.class: "nginx"    

   image:
     repository: nginx
     tag: 1.15-alpine
     pullPolicy: IfNotPresent

   hosts:
     - name: us
     - name: eu
   ```

   Example live use case
   
   ```bash
   $ helm get values ingress-test-a
   domain: gw.skymavis.xyz
   hosts:
   - name: us
   - name: eu

   $ for i in us eu;do curl -L $i.gw.skymavis.xyz;done
   us
   eu
   ```