import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AcessCodesModalComponent } from './acess-codes-modal.component';

describe('AcessCodesModalComponent', () => {
  let component: AcessCodesModalComponent;
  let fixture: ComponentFixture<AcessCodesModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AcessCodesModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AcessCodesModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
