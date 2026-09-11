/**
 * AI PRODUCT FACTORY — WEB APPLICATION ENGINE
 * Features: Client Router, State Store, LocalStorage Persistence, Zero Dead Links.
 */

(function () {
  "use strict";

  // -------------------------------------------------------------
  // 1. Initial State & Storage Management
  // -------------------------------------------------------------
  const STORAGE_KEY = "agy_product_records_v1";

  const DEFAULT_RECORDS = [
    {
      id: "REC-101",
      name: "Cloud IAM Privilege Boundary Audit",
      category: "Security",
      status: "ACTIVE",
      impact: 92,
      updated_at: new Date(Date.now() - 86400000).toISOString().split("T")[0]
    },
    {
      id: "REC-102",
      name: "Automated Evidence Harvesting Pipeline",
      category: "Architecture",
      status: "COMPLETED",
      impact: 88,
      updated_at: new Date(Date.now() - 172800000).toISOString().split("T")[0]
    },
    {
      id: "REC-103",
      name: "Continuous Compliance Telemetry Monitor",
      category: "Quality Assurance",
      status: "PENDING",
      impact: 74,
      updated_at: new Date(Date.now() - 259200000).toISOString().split("T")[0]
    }
  ];

  const state = {
    records: [],
    currentRoute: "dashboard",
    searchTerm: "",
    statusFilter: "ALL"
  };

  function loadState() {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        state.records = JSON.parse(stored);
      } else {
        state.records = [...DEFAULT_RECORDS];
        saveState();
      }
    } catch (err) {
      console.error("[Storage] Failed to read localStorage, using in-memory state:", err);
      state.records = [...DEFAULT_RECORDS];
    }
  }

  function saveState() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(state.records));
    } catch (err) {
      console.error("[Storage] Failed to write localStorage:", err);
    }
    renderMetrics();
    renderTable();
  }

  // -------------------------------------------------------------
  // 2. Client-Side Router
  // -------------------------------------------------------------
  function navigateTo(route) {
    const validRoutes = ["dashboard", "records", "settings"];
    if (!validRoutes.includes(route)) {
      route = "dashboard";
    }
    state.currentRoute = route;

    // Update Nav Links
    document.querySelectorAll(".nav-link").forEach((link) => {
      if (link.getAttribute("data-route") === route) {
        link.classList.add("active");
        link.setAttribute("aria-current", "page");
      } else {
        link.classList.remove("active");
        link.removeAttribute("aria-current");
      }
    });

    // Update Panels
    document.querySelectorAll(".view-panel").forEach((panel) => {
      if (panel.id === `view-${route}`) {
        panel.style.display = "block";
        panel.classList.add("active");
      } else {
        panel.style.display = "none";
        panel.classList.remove("active");
      }
    });

    if (route === "records") {
      renderExplorerList();
    }
  }

  function initRouter() {
    window.addEventListener("hashchange", () => {
      const hash = window.location.hash.replace("#/", "");
      navigateTo(hash || "dashboard");
    });

    // Default initial route
    const initialHash = window.location.hash.replace("#/", "");
    navigateTo(initialHash || "dashboard");
  }

  // -------------------------------------------------------------
  // 3. UI Notifications & Alerts
  // -------------------------------------------------------------
  function showAlert(message, type = "success") {
    const container = document.getElementById("alert-container");
    if (!container) return;

    const alertEl = document.createElement("div");
    alertEl.className = `alert alert-${type}`;
    alertEl.innerHTML = `
      <span>${escapeHTML(message)}</span>
      <button type="button" class="btn-close" aria-label="Dismiss">&times;</button>
    `;

    alertEl.querySelector(".btn-close").addEventListener("click", () => {
      alertEl.remove();
    });

    container.appendChild(alertEl);
    setTimeout(() => {
      alertEl.remove();
    }, 4000);
  }

  function escapeHTML(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#39;");
  }

  // -------------------------------------------------------------
  // 4. Render Logic
  // -------------------------------------------------------------
  function renderMetrics() {
    const totalEl = document.getElementById("kpi-total-records");
    const badgeEl = document.getElementById("record-count-badge");
    if (totalEl) totalEl.textContent = state.records.length;
    if (badgeEl) badgeEl.textContent = `${state.records.length} items`;
  }

  function renderTable() {
    const container = document.getElementById("table-container");
    const emptyState = document.getElementById("empty-state");
    if (!container) return;

    if (state.records.length === 0) {
      container.innerHTML = "";
      if (emptyState) emptyState.style.display = "block";
      return;
    }

    if (emptyState) emptyState.style.display = "none";

    let html = `
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Category</th>
            <th>Status</th>
            <th>Impact Score</th>
            <th>Last Updated</th>
            <th style="text-align: right;">Actions</th>
          </tr>
        </thead>
        <tbody>
    `;

    state.records.forEach((rec) => {
      const badgeClass =
        rec.status === "ACTIVE"
          ? "badge-primary"
          : rec.status === "COMPLETED"
          ? "badge-success"
          : "badge-warning";

      html += `
        <tr>
          <td><code style="font-size: 11px;">${escapeHTML(rec.id)}</code></td>
          <td><strong>${escapeHTML(rec.name)}</strong></td>
          <td>${escapeHTML(rec.category)}</td>
          <td><span class="badge ${badgeClass}">${escapeHTML(rec.status)}</span></td>
          <td>${escapeHTML(rec.impact)}/100</td>
          <td style="color: var(--color-text-muted); font-size: 12px;">${escapeHTML(rec.updated_at)}</td>
          <td style="text-align: right;">
            <button type="button" class="btn btn-secondary btn-sm" style="padding: 4px 8px; font-size: 11px;" data-action="delete" data-id="${escapeHTML(rec.id)}">
              Delete
            </button>
          </td>
        </tr>
      `;
    });

    html += `</tbody></table>`;
    container.innerHTML = html;

    // Attach row delete actions
    container.querySelectorAll('button[data-action="delete"]').forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const id = e.currentTarget.getAttribute("data-id");
        deleteRecord(id);
      });
    });
  }

  function renderExplorerList() {
    const container = document.getElementById("records-list-container");
    if (!container) return;

    let filtered = state.records.filter((r) => {
      const matchSearch =
        state.searchTerm === "" ||
        r.name.toLowerCase().includes(state.searchTerm.toLowerCase()) ||
        r.category.toLowerCase().includes(state.searchTerm.toLowerCase());
      const matchStatus = state.statusFilter === "ALL" || r.status === state.statusFilter;
      return matchSearch && matchStatus;
    });

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="card empty-state">
          <p class="text-muted">No records matched your search filter.</p>
        </div>
      `;
      return;
    }

    let html = `<div style="display: flex; flex-direction: column; gap: 12px;">`;
    filtered.forEach((rec) => {
      html += `
        <div class="card" style="margin-bottom: 0; display: flex; align-items: center; justify-content: space-between;">
          <div>
            <div style="display: flex; align-items: center; gap: 8px;">
              <strong>${escapeHTML(rec.name)}</strong>
              <span class="badge badge-neutral">${escapeHTML(rec.category)}</span>
            </div>
            <div style="font-size: 12px; color: var(--color-text-muted); margin-top: 4px;">
              ID: ${escapeHTML(rec.id)} &bull; Impact: ${escapeHTML(rec.impact)} &bull; Updated: ${escapeHTML(rec.updated_at)}
            </div>
          </div>
          <div>
            <button type="button" class="btn btn-secondary" style="padding: 4px 10px; font-size: 12px;" data-action="delete" data-id="${escapeHTML(rec.id)}">
              Delete
            </button>
          </div>
        </div>
      `;
    });
    html += `</div>`;
    container.innerHTML = html;

    container.querySelectorAll('button[data-action="delete"]').forEach((btn) => {
      btn.addEventListener("click", (e) => {
        const id = e.currentTarget.getAttribute("data-id");
        deleteRecord(id);
        renderExplorerList();
      });
    });
  }

  // -------------------------------------------------------------
  // 5. CRUD Actions
  // -------------------------------------------------------------
  function addRecord(name, category, status, impact) {
    const newRecord = {
      id: "REC-" + Math.floor(100 + Math.random() * 900),
      name: name.trim(),
      category: category,
      status: status,
      impact: parseInt(impact, 10) || 80,
      updated_at: new Date().toISOString().split("T")[0]
    };

    state.records.unshift(newRecord);
    saveState();
    showAlert(`Successfully created record: ${newRecord.name}`, "success");
  }

  function deleteRecord(id) {
    const target = state.records.find((r) => r.id === id);
    if (!target) return;

    state.records = state.records.filter((r) => r.id !== id);
    saveState();
    showAlert(`Record ${id} removed.`, "success");
  }

  // -------------------------------------------------------------
  // 6. Modal Dialog Handlers
  // -------------------------------------------------------------
  function initModal() {
    const modal = document.getElementById("modal-record");
    const openBtn = document.getElementById("btn-create-record");
    const closeBtn = document.getElementById("btn-modal-close");
    const cancelBtn = document.getElementById("btn-modal-cancel");
    const form = document.getElementById("record-form");

    function openModal() {
      if (!modal) return;
      form.reset();
      modal.style.display = "flex";
      document.getElementById("field-name").focus();
    }

    function closeModal() {
      if (!modal) return;
      modal.style.display = "none";
    }

    if (openBtn) openBtn.addEventListener("click", openModal);
    if (closeBtn) closeBtn.addEventListener("click", closeModal);
    if (cancelBtn) cancelBtn.addEventListener("click", closeModal);

    // Escape key listener
    window.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && modal && modal.style.display === "flex") {
        closeModal();
      }
    });

    if (form) {
      form.addEventListener("submit", (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        addRecord(
          formData.get("name"),
          formData.get("category"),
          formData.get("status"),
          formData.get("impact")
        );
        closeModal();
      });
    }
  }

  // -------------------------------------------------------------
  // 7. Event Attachments & Export Tools
  // -------------------------------------------------------------
  function initEvents() {
    // Refresh button
    const refreshBtn = document.getElementById("btn-refresh-stats");
    if (refreshBtn) {
      refreshBtn.addEventListener("click", () => {
        loadState();
        showAlert("Dashboard data refreshed from local storage.", "success");
      });
    }

    // Filter controls in explorer
    const searchInput = document.getElementById("search-input");
    const statusSelect = document.getElementById("filter-status");

    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        state.searchTerm = e.target.value;
        renderExplorerList();
      });
    }

    if (statusSelect) {
      statusSelect.addEventListener("change", (e) => {
        state.statusFilter = e.target.value;
        renderExplorerList();
      });
    }

    // Settings actions
    const sampleBtn = document.getElementById("btn-load-sample-data");
    const clearBtn = document.getElementById("btn-clear-storage");

    if (sampleBtn) {
      sampleBtn.addEventListener("click", () => {
        state.records = [...DEFAULT_RECORDS];
        saveState();
        showAlert("Reset records to default verified dataset.", "success");
      });
    }

    if (clearBtn) {
      clearBtn.addEventListener("click", () => {
        if (confirm("Are you sure you want to clear all records?")) {
          state.records = [];
          saveState();
          showAlert("All local application state cleared.", "danger");
        }
      });
    }

    // Export JSON
    const exportJsonBtn = document.getElementById("btn-export-json");
    if (exportJsonBtn) {
      exportJsonBtn.addEventListener("click", () => {
        const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(state.records, null, 2));
        const downloadAnchor = document.createElement("a");
        downloadAnchor.setAttribute("href", dataStr);
        downloadAnchor.setAttribute("download", "application_records.json");
        document.body.appendChild(downloadAnchor);
        downloadAnchor.click();
        downloadAnchor.remove();
        showAlert("Exported records as JSON.", "success");
      });
    }

    // Export CSV
    const exportCsvBtn = document.getElementById("btn-export-csv");
    if (exportCsvBtn) {
      exportCsvBtn.addEventListener("click", () => {
        const headers = ["id", "name", "category", "status", "impact", "updated_at"];
        let csvContent = headers.join(",") + "\n";
        state.records.forEach((r) => {
          csvContent += `"${r.id}","${r.name.replace(/"/g, '""')}","${r.category}","${r.status}",${r.impact},"${r.updated_at}"\n`;
        });
        const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
        const url = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.setAttribute("href", url);
        link.setAttribute("download", "application_records.csv");
        document.body.appendChild(link);
        link.click();
        link.remove();
        showAlert("Exported records as CSV.", "success");
      });
    }
  }

  // -------------------------------------------------------------
  // 8. Bootstrap
  // -------------------------------------------------------------
  document.addEventListener("DOMContentLoaded", () => {
    loadState();
    initRouter();
    initModal();
    initEvents();
    renderMetrics();
    renderTable();
    console.log("[AI Product Factory] Web Application Initialized Successfully.");
  });
})();
