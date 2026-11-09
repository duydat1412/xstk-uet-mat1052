import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

tree_css = """
/* ==========================================================================
   UI/UX PRO MAX: FOLDER TREE SIDEBAR NAVIGATION (LEFT COLUMN)
   ========================================================================== */
.study-layout {
  display: flex;
  gap: 24px;
  max-width: 1400px;
  margin: 0 auto;
  padding: 20px 20px 60px;
  align-items: flex-start;
}

/* SIDEBAR FOLDER TREE */
.sidebar-folder-tree {
  width: 320px;
  flex-shrink: 0;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-lg);
  padding: 16px;
  position: sticky;
  top: 76px;
  max-height: calc(100vh - 96px);
  overflow-y: auto;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  z-index: 40;
}
.sidebar-folder-tree::-webkit-scrollbar {
  width: 5px;
}
.sidebar-folder-tree::-webkit-scrollbar-thumb {
  background: var(--line);
  border-radius: 10px;
}
.sidebar-folder-tree::-webkit-scrollbar-thumb:hover {
  background: var(--mute);
}

.tree-header {
  border-bottom: 1px solid var(--line);
  padding-bottom: 12px;
  margin-bottom: 12px;
}
.tree-title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
}
.tree-main-title {
  font-size: 0.95rem;
  font-weight: 800;
  color: var(--ink);
  display: flex;
  align-items: center;
  gap: 8px;
}
.tree-badge-total {
  font-size: 0.75rem;
  font-weight: 700;
  background: var(--acc-soft);
  color: var(--acc);
  padding: 2px 8px;
  border-radius: 10px;
}
.tree-close-drawer-btn {
  display: none;
  background: none;
  border: none;
  font-size: 1.2rem;
  color: var(--mute);
  cursor: pointer;
  padding: 4px;
}
.tree-search-input {
  width: 100%;
  padding: 8px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--line);
  background: var(--card-sub);
  color: var(--ink);
  font-size: 0.85rem;
  outline: none;
  transition: all 0.15s ease;
  box-sizing: border-box;
}
.tree-search-input:focus {
  border-color: var(--acc);
  background: var(--card);
  box-shadow: 0 0 0 3px var(--acc-soft);
}

/* FOLDER ITEM */
.tree-folder {
  margin-bottom: 8px;
}
.tree-folder-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 9px 10px;
  border-radius: var(--radius-sm);
  cursor: pointer;
  user-select: none;
  font-size: 0.86rem;
  font-weight: 700;
  color: var(--ink);
  transition: all 0.15s ease;
}
.tree-folder-head:hover {
  background: var(--card-sub);
}
.tree-folder-left {
  display: flex;
  align-items: center;
  gap: 7px;
  flex: 1;
  min-width: 0;
}
.tree-arrow {
  font-size: 0.72rem;
  color: var(--mute);
  transition: transform 0.2s ease;
  display: inline-block;
  width: 12px;
  text-align: center;
}
.tree-folder.open .tree-arrow {
  transform: rotate(90deg);
}
.tree-folder-icon {
  font-size: 1rem;
  line-height: 1;
}
.tree-folder-title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.tree-folder-badge {
  font-size: 0.72rem;
  font-weight: 700;
  padding: 2px 6px;
  border-radius: 8px;
  background: var(--card-sub);
  color: var(--mute);
  white-space: nowrap;
}

/* FOLDER LESSONS LIST */
.tree-folder-list {
  display: none;
  margin-left: 14px;
  padding-left: 10px;
  border-left: 2px dashed var(--line);
  margin-top: 3px;
  margin-bottom: 6px;
}
.tree-folder.open .tree-folder-list {
  display: block;
}

.tree-lesson-btn {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  text-align: left;
  padding: 7px 10px;
  border-radius: var(--radius-sm);
  background: transparent;
  border: 1px solid transparent;
  color: var(--mute);
  font-size: 0.84rem;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 2px;
  transition: all 0.15s ease;
  gap: 8px;
  box-sizing: border-box;
}
.tree-lesson-btn:hover {
  color: var(--ink);
  background: var(--card-sub);
}
.tree-lesson-btn.active {
  background: var(--acc-soft);
  color: var(--acc);
  border-color: rgba(59, 130, 246, 0.3);
  font-weight: 700;
}
.tree-lesson-left {
  display: flex;
  align-items: center;
  gap: 6px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.tree-status-icon {
  font-size: 0.78rem;
  color: var(--mute);
  flex-shrink: 0;
}
.tree-lesson-btn.done .tree-status-icon {
  color: var(--ok);
  font-weight: 800;
}

/* MAIN CONTENT WRAP */
.main-content-wrap {
  flex: 1;
  min-width: 0;
  max-width: 980px;
}

/* MOBILE DRAWER & BAR */
.mobile-tree-bar {
  display: none;
  margin-bottom: 16px;
}
.mobile-tree-btn {
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: var(--radius-md);
  padding: 11px 16px;
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--ink);
  cursor: pointer;
  box-shadow: var(--shadow-sm);
}
.tree-drawer-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(2px);
  z-index: 90;
}

@media (max-width: 960px) {
  .study-layout {
    flex-direction: column;
    padding: 12px 12px 40px;
  }
  .main-content-wrap {
    max-width: 100%;
    width: 100%;
  }
  .mobile-tree-bar {
    display: block;
  }
  .sidebar-folder-tree {
    position: fixed;
    top: 0;
    left: 0;
    height: 100vh;
    max-height: 100vh;
    width: 310px;
    z-index: 100;
    border-radius: 0;
    box-shadow: var(--shadow-lg);
    transform: translateX(-105%);
    transition: transform 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .sidebar-folder-tree.drawer-open {
    transform: translateX(0);
  }
  .tree-close-drawer-btn {
    display: block;
  }
  .tree-drawer-overlay.active {
    display: block;
  }
}
"""

tree_js_code = """
// ==========================================================================
// FOLDER TREE NAVIGATION LOGIC (UI/UX PRO MAX)
// ==========================================================================
let openFolders = {};
let treeSearchQuery = '';

function initFolderState() {
  const curLesson = ALL_LESSONS[curLessonIdx];
  if (curLesson) {
    openFolders[curLesson.cluster] = true;
  }
}

function toggleFolder(clusterKey, event) {
  if (event) event.stopPropagation();
  openFolders[clusterKey] = !openFolders[clusterKey];
  renderFolderTree();
}

function filterTreeLessons(query) {
  treeSearchQuery = (query || '').trim().toLowerCase();
  if (treeSearchQuery) {
    // Tự động mở tất cả các folder khi đang tìm kiếm
    Object.keys(CLUSTER_NAMES).forEach(c => { openFolders[c] = true; });
  }
  renderFolderTree();
}

function toggleMobileTree() {
  const sidebar = document.getElementById('sidebarTree');
  const overlay = document.getElementById('treeOverlay');
  if (!sidebar) return;
  const isOpen = sidebar.classList.contains('drawer-open');
  if (isOpen) {
    sidebar.classList.remove('drawer-open');
    if (overlay) overlay.classList.remove('active');
  } else {
    sidebar.classList.add('drawer-open');
    if (overlay) overlay.classList.add('active');
  }
}

function closeMobileTree() {
  const sidebar = document.getElementById('sidebarTree');
  const overlay = document.getElementById('treeOverlay');
  if (sidebar) sidebar.classList.remove('drawer-open');
  if (overlay) overlay.classList.remove('active');
}

function renderFolderTree() {
  const container = document.getElementById('treeFolderContainer');
  if (!container) return;

  const countBadge = document.getElementById('treeLessonCount');
  if (countBadge) {
    countBadge.textContent = `${ALL_LESSONS.length} bài`;
  }

  // Cập nhật tiêu đề trên mobile bar
  const mobileTitle = document.getElementById('mobileCurLessonTitle');
  if (mobileTitle && ALL_LESSONS[curLessonIdx]) {
    const l = ALL_LESSONS[curLessonIdx];
    mobileTitle.textContent = `${l.id}: ${l.title.split(':')[0]}`;
  }

  // Nhóm các bài học theo cụm
  const grouped = {};
  Object.keys(CLUSTER_NAMES).forEach(c => { grouped[c] = []; });
  ALL_LESSONS.forEach((l, idx) => {
    if (!grouped[l.cluster]) grouped[l.cluster] = [];
    grouped[l.cluster].push({ ...l, globalIdx: idx });
  });

  let html = '';

  Object.keys(grouped).forEach(clusterKey => {
    const clusterLessons = grouped[clusterKey] || [];
    if (clusterLessons.length === 0) return;

    // Lọc theo search query nếu có
    const filteredLessons = clusterLessons.filter(l => {
      if (!treeSearchQuery) return true;
      return l.title.toLowerCase().includes(treeSearchQuery) ||
             l.id.toLowerCase().includes(treeSearchQuery);
    });

    if (treeSearchQuery && filteredLessons.length === 0) return;

    const clusterTitle = CLUSTER_NAMES[clusterKey] || `Cụm ${clusterKey}`;
    const isOpen = !!openFolders[clusterKey] || !!treeSearchQuery;
    
    // Đếm số bài đã hoàn thành trong cụm
    const doneCount = clusterLessons.filter(l => !!completedLessons[l.id]).length;
    const isClusterDone = doneCount === clusterLessons.length && clusterLessons.length > 0;

    html += `
      <div class="tree-folder ${isOpen ? 'open' : ''}">
        <div class="tree-folder-head" onclick="toggleFolder('${clusterKey}', event)">
          <div class="tree-folder-left">
            <span class="tree-arrow">▶</span>
            <span class="tree-folder-icon">${isOpen ? '📂' : '📁'}</span>
            <span class="tree-folder-title" title="${clusterTitle}">${clusterTitle}</span>
          </div>
          <span class="tree-folder-badge ${isClusterDone ? 'done-badge' : ''}" style="${isClusterDone ? 'color:var(--ok);background:var(--ok-soft);' : ''}">
            ${isClusterDone ? '✓ ' : ''}${doneCount}/${clusterLessons.length}
          </span>
        </div>
        <div class="tree-folder-list">
    `;

    filteredLessons.forEach(l => {
      const isDone = !!completedLessons[l.id];
      const isActive = l.globalIdx === curLessonIdx;
      html += `
        <button class="tree-lesson-btn ${isActive ? 'active' : ''} ${isDone ? 'done' : ''}" 
                onclick="goToLesson(${l.globalIdx}); closeMobileTree();"
                title="${l.title}">
          <div class="tree-lesson-left">
            <span class="tree-status-icon">${isDone ? '✓' : (isActive ? '👉' : '📄')}</span>
            <span style="font-size:0.8rem;font-weight:700;">${l.id}:</span>
            <span style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">${l.title.split(':')[0]}</span>
          </div>
        </button>
      `;
    });

    html += `
        </div>
      </div>
    `;
  });

  if (html === '' && treeSearchQuery) {
    html = `<div style="padding:16px;text-align:center;color:var(--mute);font-size:0.88rem;">Không tìm thấy bài học nào phù hợp với từ khóa "${treeSearchQuery}".</div>`;
  }

  container.innerHTML = html;
}
"""

def update_page_to_folder_tree(filepath, is_csdl=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Insert CSS
    if 'UI/UX PRO MAX: FOLDER TREE SIDEBAR NAVIGATION' not in html:
        html = html.replace('</style>', tree_css + '\n</style>')

    # 2. Replace the main layout
    # Currently:
    # <main>
    #   <div class="clusters-nav" id="clusterTabs"> ... </div>
    #   <div class="lessons-strip" id="lessonsStrip"></div>
    #   <div class="card" id="lessonCard"> ... </div>
    # </main>
    
    old_layout_pattern = r'<main>\s*<!-- CLUSTERS TABS -->[\s\S]*?<div class="card" id="lessonCard">'
    
    new_layout = """
<!-- TREE DRAWER OVERLAY FOR MOBILE -->
<div class="tree-drawer-overlay" id="treeOverlay" onclick="closeMobileTree()"></div>

<div class="study-layout">
  <!-- LEFT SIDEBAR: FOLDER TREE NAVIGATION -->
  <aside class="sidebar-folder-tree" id="sidebarTree">
    <div class="tree-header">
      <div class="tree-title-row">
        <div class="tree-main-title">
          <span>📁</span>
          <span>Mục Lục Bài Học</span>
        </div>
        <div style="display:flex;align-items:center;gap:6px;">
          <span class="tree-badge-total" id="treeLessonCount">14 bài</span>
          <button class="tree-close-drawer-btn" onclick="closeMobileTree()" aria-label="Đóng danh mục">✕</button>
        </div>
      </div>
      <input type="text" class="tree-search-input" id="treeSearchInput" placeholder="🔍 Tìm kiếm bài học..." oninput="filterTreeLessons(this.value)">
    </div>
    
    <!-- DYNAMIC TREE FOLDERS -->
    <div class="tree-body" id="treeFolderContainer" style="flex:1;"></div>
  </aside>

  <!-- RIGHT: MAIN LESSON CONTENT -->
  <main class="main-content-wrap">
    <!-- MOBILE DRAWER TOGGLE BAR -->
    <div class="mobile-tree-bar">
      <button class="mobile-tree-btn" onclick="toggleMobileTree()">
        <span style="display:flex;align-items:center;gap:8px;">
          <span>📑</span>
          <span id="mobileCurLessonTitle">Danh mục bài học</span>
        </span>
        <span class="mobile-tree-arrow">▾ Xem tất cả</span>
      </button>
    </div>

    <!-- MAIN LESSON CARD -->
    <div class="card" id="lessonCard">
"""

    if re.search(old_layout_pattern, html):
        html = re.sub(old_layout_pattern, new_layout.strip(), html)
        print(f"Replaced main layout in {filepath}")
    else:
        print(f"Warning: Could not match old layout in {filepath}")

    # 3. Add JS functions
    if 'renderFolderTree' not in html:
        # Insert before renderCurrentLesson
        html = html.replace('function renderCurrentLesson() {', tree_js_code + '\nfunction renderCurrentLesson() {')
        print(f"Added tree JS functions to {filepath}")

    # 4. Update calls: Replace renderLessonsStrip() and renderClusterTabs() with renderFolderTree()
    html = re.sub(r'renderClusterTabs\(\);', 'initFolderState(); renderFolderTree();', html)
    html = re.sub(r'renderLessonsStrip\(\);', 'renderFolderTree();', html)

    # 5. Fix cluster names for CSDL if needed
    if is_csdl:
        csdl_cluster_names = """
const CLUSTER_NAMES = {
  "1": "Cụm 1: Tổng quan & Mô hình ER/EER (4 bài)",
  "2": "Cụm 2: Mô hình Quan hệ & Ánh xạ (2 bài)",
  "3": "Cụm 3: Đại số Quan hệ (3 bài)",
  "4": "Cụm 4: Phụ thuộc hàm & Chuẩn hóa (5 bài)"
};
"""
        html = re.sub(r'const CLUSTER_NAMES = \{[\s\S]*?\};', csdl_cluster_names.strip(), html)
    else:
        xstk_cluster_names = """
const CLUSTER_NAMES = {
  "A": "Cụm A: Dữ liệu & Thống kê mô tả (5 bài)",
  "B": "Cụm B: Lý thuyết Xác suất & Đếm (5 bài)",
  "C": "Cụm C: Biến ngẫu nhiên rời rạc (6 bài)",
  "D": "Cụm D: Tổng, Trung bình & Luật số lớn (4 bài)",
  "E": "Cụm E: Biến liên tục & CLT (6 bài)"
};
"""
        html = re.sub(r'const CLUSTER_NAMES = \{[\s\S]*?\};', xstk_cluster_names.strip(), html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Successfully upgraded {filepath} to Folder Tree Navigation!")

# Update both files
update_page_to_folder_tree('site/csdl/hoc.html', is_csdl=True)
update_page_to_folder_tree('site/hoc.html', is_csdl=False)
