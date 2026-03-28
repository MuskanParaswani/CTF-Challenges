This challenge simulates insecure role validation combined with weak MD5-based admin token verification.

Users must:

1. Intercept the POST request using Burp Suite.
2. Modify role from user to admin.
3. Generate a valid admin token.
4. Add custom header.
5. Retrieve dynamic flag.

## Features

- Dynamic flag generation (rotates every 30 minutes)
- MD5-based admin token validation
- Custom header requirement
- Role escalation vulnerability
- Burp Suite exploitation required