1. Write an application/script that accepts a list of Quay image references. Your application needs to print out a list of vulnerabilities for each image in the list. Please submit a link to a public GitHub repository with the source code of your solution. As an alternative, you may send a tar archive by email, but this is discouraged
   
   - Read json from file or stdin
   - Array of repo object, for example: 
     ```json 
     [
       {
		"Organisation":"coreos",
		"Repository":"hyperkube",
		"Tag":"v1.10.4_coreos.0"
       },
       {
		"Organisation":"coreos",
		"Repository":"dnsmasq",
		"Tag":"v0.5.0"
       },
     ]
     ```
   - Document any other parameters/env vars you may need
   - Refer to https://docs.quay.io/api/swagger/ `secscan` API endpoints
   
   Output:
   
   a json array with the name of the repository, the tag, the manifest id, and an array of vulnerabilities
   for example (some array elements omitted for clarity):
   
   ```json
	[
	  {
	    "Organisation": "coreos",
	    "Repository": "hyperkube",
	    "Tag": "v1.10.4_coreos.0",
	    "Manifest": "sha256:ced8ba1345b8fef845ab256b7b4d0634423363721afe8f306c1a4bc4a75d9a0c",
	    "Vulnerabilities": [
	      {
		"PackageName": "sqlite3",
		"Severity": "Medium",
		"NamespaceName": "debian:9",
		"Link": "https://security-tracker.debian.org/tracker/CVE-2018-8740",
		"Description": "In SQLite through 3.22.0, databases whose schema is corrupted using a CREATE TABLE AS statement could cause a NULL pointer dereference, related to build.c and prepare.c.",
		"Name": "CVE-2018-8740",
		"Metadata": {
		  "NVD": {
		    "CVSSv2": {
		      "Score": 5,
		      "Vectors": "AV:N/AC:L/Au:N/C:N/I:N"
		    }
		  }
		}
	      },
	      {
		"PackageName": "sqlite3",
		"Severity": "Negligible",
		"NamespaceName": "debian:9",
		"Link": "https://security-tracker.debian.org/tracker/CVE-2017-13685",
		"Description": "The dump_callback function in SQLite 3.20.0 allows remote attackers to cause a denial of service (EXC_BAD_ACCESS and application crash) via a crafted file.",
		"Name": "CVE-2017-13685",
		"Metadata": {
		  "NVD": {
		    "CVSSv2": {
		      "Score": 4.3,
		      "Vectors": "AV:N/AC:M/Au:N/C:N/I:N"
		    }
		  }
		}
	      }
	    ]
	  },
	  {
	    "Organisation": "coreos",
	    "Repository": "dnsmasq",
	    "Tag": "v0.5.0",
	    "Manifest": "sha256%3A910710beddb9cf3a01fe36450b4188b160a03608786c11e0c39b81f570f55377",
	    "Vulnerabilities": [
	      {
		"PackageName": "busybox",
		"Name": "CVE-2017-15873",
		"NamespaceName": "alpine:v3.6",
		"Link": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-15873",
		"FixedBy": "1.26.2-r9",
		"Severity": "Medium",
		"Metadata": {
		  "NVD": {
		    "CVSSv2": {
		      "Score": 4.3,
		      "Vectors": "AV:N/AC:M/Au:N/C:N/I:N"
		    }
		  }
		}
	      },
	      {
		"PackageName": "busybox",
		"Name": "CVE-2017-16544",
		"NamespaceName": "alpine:v3.6",
		"Link": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-16544",
		"FixedBy": "1.26.2-r9",
		"Severity": "Medium",
		"Metadata": {
		  "NVD": {
		    "CVSSv2": {
		      "Score": 6.5,
		      "Vectors": "AV:N/AC:L/Au:S/C:P/I:P"
		    }
		  }
		}
	      },
	      {
		"PackageName": "musl",
		"Name": "CVE-2017-15650",
		"NamespaceName": "alpine:v3.6",
		"Link": "https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-15650",
		"FixedBy": "1.1.16-r14",
		"Severity": "Medium",
		"Metadata": {
		  "NVD": {
		    "CVSSv2": {
		      "Score": 5,
		      "Vectors": "AV:N/AC:L/Au:N/C:N/I:N"
		    }
		  }
		}
	      }
	    ]
	  }
	]
   ```
   
   **note** Vulnerabilities of different packages are merged into a single list!