import { Component, OnDestroy, inject } from '@angular/core';
import { CommonModule, NgIf } from '@angular/common';
import { RouterLink } from '@angular/router';
import { Subscription } from 'rxjs';

import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, NgIf, RouterLink],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnDestroy {
  private authService = inject(AuthService);
  isLoggedIn = false;
  menuOpen = false;
  private sub: Subscription;

  constructor() {
    this.sub = this.authService.isLoggedIn$.subscribe((val: boolean) => {
      console.log('Usuário logado', val);
      this.isLoggedIn = val;
      if (!val) this.menuOpen = false;
    });
  }

  toggleMenu(): void {
    this.menuOpen = !this.menuOpen;
  }

  onLogout(): void {
    this.authService.logout();
  }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }
}
