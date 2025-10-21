---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: Kushal Pokharel
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/Kushal_CV_sem2.pdf
      headings:
        about: ""
        education: ""
        interests: ""
    design:
      # Apply a gradient background
      css_class: hbx-bg-gradient
      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: markdown
    content:
      title: "📚 My Research"
      subtitle: ""
      text: |-
        I am working on Trust minimization on a single party using Cryptography. Secure multiparty communication protocols help to minimize the trust on one single entity and distribute it among the participating entities. It can find its application in fields like Federated Learning but the cost of communication and computation in the devices increases. Is it possible to optimize the computation burden to a negligible level that users readily trade for enhanced trustlessness?

        On the other hand, I constantly keep up with new algorithms that are being developed and standardized as a part of defense against quantum computers. Most of these cryptosystems are based on Lattices and problems on Lattices. However, while being resistant to the quantum computers' attack, they can become vulnerable to other side channel attacks. I am actively working on identifying such attacks and defenses.
    design:
      columns: "1"
---
